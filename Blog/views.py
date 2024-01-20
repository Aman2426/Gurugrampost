
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy,reverse
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from .models import Article, Category, Vote, Comment
from .forms import CategoryForm, ArticleForm, CommentForm
from .utils import ObjectCreateMixin, ObjectUpdateMixin
from django.contrib.auth.views import LoginView
from django.template import loader,Context
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.decorators import permission_required, \
                                            login_required
import datetime


# Create your views here.

# Article List

#@permission_required('Blog.view_article')
def article_list(request):
    template="Blog/article_list.html"
    article_list=Article.objects.all()
    ctx={"article_list":article_list}
    return render(request,template,ctx)

# Article Detail

def article_detail(request,year,month,slug):  
    
    template="Blog/article_detail.html"

    article=get_object_or_404(
        Article, 
        date_pub__year=year, 
        date_pub__month=month, 
        slug__iexact=slug)
    
    comments=article.comments.filter(parent=None,).reverse()

    articles=Article.objects.all()[:7]
    
    if request.method == 'GET':
        comment_form=CommentForm()

        ctx={
            "article":article,
            'articles':articles,
            'comment_form':comment_form,
            'comments':comments,
            }
        
        return render(request,template,ctx)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.parent=None
            comment.save()
            messages.success(request,'Comment Added')
            return redirect(article)
        else:
            return redirect('users:login')

# Article Create

class ArticleCreate(ObjectCreateMixin, View):
    form_class = ArticleForm
    template_name = 'Blog/article_create.html'

# Article Update

class ArticleUpdate(ObjectUpdateMixin, View):
    form_class = ArticleForm
    template_name = 'Blog/article_update.html'
    model = Article

# View to delete article 

def article_delete(request, year, month, slug): # perhaps make this a class
    
    obj = get_object_or_404(
        Article, 
        date_pub__year=year, 
        date_pub__month=month, 
        slug__iexact=slug)
    
    if request.method == 'GET':
        
        return render(request,"Blog/article_delete.html", {'article':obj} )

    if request.method == "POST":

        obj.delete()
        return redirect('blog:article_list')

# Category List

def cat_list(request):
    template="Blog/cat_list.html"
    cat_list=Category.objects.all()
    ctx={"cat_list":cat_list}
    return render(request,template,ctx)

# Category Detail

def cat_detail(request,slug):
    template="Blog/cat_detail.html"
    cat=Category.objects.get(slug__iexact=slug)
    ctx={"cat":cat}
    return render(request,template,ctx)

# Category Create

def cat_create(request):  # This is the manual version. The same is done by ObjectCreateMixin Class for Author and Article right below it. 
    if request.method == 'POST':
        form = CategoryForm(request.POST)       #Category still needs to be cleaned, as @ and % cannot be categories. 
        if form.is_valid():
            new_tag = form.save()
            return redirect(new_tag)
    else:  # request.method != 'POST'
        form = CategoryForm()
    return render(
        request,
        'Blog/category_form.html',
        {'form': form})

# Category Update

class CategoryUpdate(View):
    form_class = CategoryForm
    template_name = 'Blog/category_update.html'
    model = Category

    def get_object(self, slug):
        return get_object_or_404(self.model, slug=slug)

    def get(self, request, slug): 
        category = self.get_object(slug)
        context={'form':self.form_class(instance=category)}
        return render(request, self.template_name, context)

    def post(self, request, slug):
        category = self.get_object(slug)
        bound_form= self.form_class(request.POST, instance=category)
        if bound_form.is_valid():
            new_category= bound_form.save()
            return redirect(new_category)
        else: 
            context={'form':bound_form,'category':category}
            return render(request, self.template_name, context)

        
# Article Votes  

@login_required
def vote(request,pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        if not Vote.objects.filter(user=request.user, article=article).exists():
            Vote.objects.create(user=request.user, article=article)
            messages.success(request, 'Your vote has been counted.')
        else:
            messages.warning(request, 'You already voted on this article.')
    return redirect(article)


# Articles Comment 

def reply_comment(request, pk):
    reply_comment = get_object_or_404(Comment, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = reply_comment.article
            comment.parent = reply_comment
            comment.user = request.user
            comment.save()
            return redirect(reply_comment.article)

# Edit Comment

def edit_comment(request, pk):
    comment = get_object_or_404(Comment,pk=pk)
    if request.method == 'POST':
        bound_form = CommentForm(request.POST,instance=comment)
        if bound_form.is_valid():
            bound_form.save()
            return redirect('blog:article_detail')
        
    if request.method == "GET":
        bound_form = CommentForm(instance=comment)
        return render(request,'Blog/edit_comment.html',{'bound_form':bound_form})


# Delete Comment

def delete_comment(request, id):
    pass







  
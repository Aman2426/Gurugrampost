
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import permission_required,login_required
import datetime
from .forms import CreateUserForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})


def login_page(request):

    if request.user.is_authenticated:
        return redirect('blog:article_list')

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request,'Login successful for {}'.format(username))
            return redirect('blog:article_list')
        else:
            messages.info(request,'Wrong credentials')
    context ={}
    return render (request, "accounts/login.html", context)


def register_page(request):
    
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data['username']
            messages.success(request, 'Account was succesfully created for {}'.format(user))
            return redirect('users:login')
        else:
            print(form.is_bound)
            print(request.POST)
            context = {'form':form}
            return render (request, "users/register.html", context)
    context = {'form':form}
    return render (request, "users/register.html", context)

def logout_page(request):
    logout(request)
    return redirect('users:login')

def user_page(request):
    context={}
    return render(request, "users/user_page.html", context)

class Login(LoginView):
    template_name = "accounts/login2.html"
    next_page = reverse_lazy("blog:article_list")
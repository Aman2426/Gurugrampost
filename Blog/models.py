
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
import datetime as datetime
from users.models import Profile
from ckeditor.fields import RichTextField


# Create your models here.

class Bookmark(models.Model):
    article=models.ForeignKey('Article',on_delete=models.CASCADE)
    user=models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user.username} Bookmarked {self.article.title}'

class Article(models.Model):
    title=models.CharField(max_length=100)
    date_pub=models.DateTimeField("Published DateTime",auto_now_add=True) #auto_now_add is for adding date when first created, not whenever updated
    author=models.ForeignKey(get_user_model(),on_delete=models.CASCADE) 
    cat=models.ManyToManyField("Category",verbose_name="Category")
    text=RichTextField()
    img=models.ImageField(verbose_name='Cover Image',null=True,blank=True)
    slug=models.SlugField(max_length=50, unique_for_month="date_pub")    #must include only lowercase alphanumeric characters and dashes
    updated_at=models.DateTimeField("Updated on",auto_now=True)
    featured=models.BooleanField(verbose_name='Home Page(Featured)',default=False)
    section=models.ForeignKey('Section',on_delete=models.CASCADE,default=None,null=True)

    class Meta:
        ordering = ('-date_pub',)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:article_detail", kwargs={'year':self.date_pub.year,'month':self.date_pub.month,'slug':self.slug})

    def get_update_url(self):
        return reverse("blog:article_update", kwargs={'pk':self.pk})
    
    def get_delete_url(self):
        return reverse("blog:article_delete", kwargs={'year':self.date_pub.year,'month':self.date_pub.month,'slug':self.slug})

    def was_published_recently(self): # Watch Out!
        return self.date_pub >= timezone.now() - datetime.timedelta(days=1)


class Category(models.Model):
    cat_name=models.CharField(max_length=45, unique=True)
    slug=models.SlugField(max_length=30,unique=True)
    img=models.ImageField(blank=True)

    def get_absolute_url(self):
        return reverse("blog:cat_detail", kwargs={'slug':self.slug})

    def get_update_url(self):
        return reverse("blog:category_update", kwargs={'slug':self.slug})

    def __str__(self):
        return self.cat_name

class Section(models.Model):
    name=models.CharField(max_length=45, unique=True)
    slug=models.SlugField(max_length=30,unique=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('blog:section_view',kwargs={'slug':self.slug})


class Vote(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('article', 'user',)

class Comment(models.Model):
    
    
    article = models.ForeignKey(
        Article, 
        on_delete=models.CASCADE, 
        related_name='comments')
    
    user = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE)
    
    text = models.TextField()
    
    created_date = models.DateTimeField(auto_now_add=True)

    parent = models.ForeignKey('Comment',on_delete=models.DO_NOTHING,null=True,blank=True)

    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return f'{self.user.username} commented {self.text[:10]} on {self.article.title}'
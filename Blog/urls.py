from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings #add this
from django.conf.urls.static import static #add this

app_name = "blog"

urlpatterns = [

    path('articles/create', views.ArticleCreate.as_view(), name="article_create"),
    path('articles/<int:year>/<int:month>/<slug:slug>',views.article_detail, name="article_detail"),
    path('articles/update/<int:pk>',views.ArticleUpdate.as_view(), name="article_update"),
    path('articles/delete/<int:year>/<int:month>/<slug:slug>',views.article_delete, name="article_delete"),
    path("articles/", views.article_list,name="article_list"),

    path('category/create', views.cat_create, name='cat_create'),
    path('category/update/<slug:slug>', views.CategoryUpdate.as_view(), name='category_update'),  #may have to change urlpattern
    path('category/<slug:slug>', views.cat_detail, name='cat_detail'),
    path("categories", views.cat_list, name="cat_list"),
    path("section/<slug:slug>", views.section_view, name="section_view"),
    
    path("vote/<int:pk>", views.vote, name="vote"),
    path("reply/<int:pk>", views.reply_comment, name="reply_comment"),
    path("edit_comment/<int:pk>", views.edit_comment, name="edit_comment"),
    path("bookmark/<int:pk>", views.bookmark, name="bookmark"),

    path("control_center", views.control_center, name="control_center"),
    path("toggle_featured/<int:pk>", views.toggle_featured, name="toggle_featured"),
    
] 

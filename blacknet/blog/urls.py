from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index,name="blogHome"),
    path('blogpost/<int:id>', views.blogpost,name="blogPost"),
    path('post/', views.post,name="Post"),
]
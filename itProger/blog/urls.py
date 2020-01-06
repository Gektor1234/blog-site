
from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('', views.ShowNewsView.as_view(), name="blog-home"),
    path('posts/<int:pk>/', views.NewsDetailView.as_view(), name="posts-detail"),
    path('posts/<str:username>/', views.UserAllNewsView.as_view(), name="user-posts"),
    path('posts/add/', views.CreateNewsView.as_view(), name="posts-add"),
    path('posts/<int:pk>/update/', views.UpdateNewsView.as_view(), name="posts-update"),
    path('posts/<int:pk>/delete/', views.DeleteNewsView.as_view(), name="posts-delete"),
    path('contacti/', views.contacti, name="blog-contacti"),

]

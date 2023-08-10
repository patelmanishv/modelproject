# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # URL for listing all posts
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  # URL for post details with a primary key as parameter
    path('user/<str:username>/', views.user_profile, name='user_profile'),  # URL for user profiles with username as parameter
]

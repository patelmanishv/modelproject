# blog/views.py

from django.shortcuts import render, get_object_or_404
from .models import Post, UserProfile

# View to list all posts
def post_list(request):
    posts = Post.objects.all()  # Retrieve all posts from the database
    return render(request, 'blog/post_list.html', {'posts': posts})  # Render the 'post_list.html' template with posts data

# View to display details of a specific post
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)  # Retrieve the specific post with the given primary key or return a 404 error
    return render(request, 'blog/post_detail.html', {'post': post})  # Render the 'post_detail.html' template with post data

# View to display user profiles
def user_profile(request, username):
    user_profile = get_object_or_404(UserProfile, user__username=username)  # Retrieve the user profile with the given username or return a 404 error
    return render(request, 'blog/user_profile.html', {'user_profile': user_profile})  # Render the 'user_profile.html' template with user profile data

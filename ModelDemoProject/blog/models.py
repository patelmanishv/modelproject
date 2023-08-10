# blog/models.py

from django.db import models
from django.contrib.auth.models import User

# Define a model for user profiles with a One-to-One relationship to the built-in User model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # One-to-One relationship with User model
    bio = models.TextField()  # User's biography
    profile_picture = models.ImageField(upload_to='profilepics/')  # Profile picture with file upload to 'profile_pics/' directory

# Define a model for tags
class Tag(models.Model):
    name = models.CharField(max_length=50)  # Tag name

# Define a model for posts with relationships to User and Tag models
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Many-to-One relationship with User model
    title = models.CharField(max_length=200)  # Post title
    content = models.TextField()  # Post content
    tags = models.ManyToManyField(Tag)  # Many-to-Many relationship with Tag model
    pub_date = models.DateTimeField(auto_now_add=True)  # Publication date of the post

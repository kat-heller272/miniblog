from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Posts(models.Model):
    author = models.ForeignKey('Blogger', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    blog_text = models.TextField(help_text="Blog post here")

class Comment(models.Model):
    post = models.ForeignKey('Posts', on_delete=models.PROTECT)
    date = models.DateField(auto_now_add=True)
    comment_text = models.TextField(help_text="Comment text goes here")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Blogger(models.Model):
    date_of_birth = models.DateField(help_text="Enter your birthday")
    city = models.CharField(max_length=30, help_text="Enter the city you live in")
    state = models.CharField(help_text="Enter the state you live in")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=300, help_text="Write a little about yourself", null=True)
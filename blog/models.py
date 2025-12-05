from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('Blogger', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    blog_text = models.TextField(help_text="Blog post here")
    title = models.CharField(max_length=40, help_text="Enter a title")

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.PROTECT)
    date = models.DateField(auto_now_add=True)
    comment_text = models.TextField(help_text="Comment text goes here")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"Comment by {self.user} on {self.post.title}"

class Blogger(models.Model):
    date_of_birth = models.DateField(help_text="Enter your birthday")
    city = models.CharField(max_length=30, help_text="Enter the city you live in")
    state = models.CharField(max_length=25, help_text="Enter the state you live in")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=300, help_text="Write a little about yourself", null=True)
    first_joined = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-first_joined']

    def __str__(self):
        return f"{self.user.username} - {self.user.get_full_name()}"
    
    def get_location(self):
        return f"{self.city}, {self.state}"
    
    def get_absolute_url(self):
        return reverse('blogger-detail', args=[str(self.id)])
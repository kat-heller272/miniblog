from django.contrib import admin

# Register your models here.
from .models import Post, Comment, Blogger

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post')

@admin.register(Blogger)
class BloggerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'user', 'first_joined')

    def full_name(self, obj):
        return obj.user.get_full_name()
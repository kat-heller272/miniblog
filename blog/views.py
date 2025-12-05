from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404

# Create your views here.
from .models import Post, Comment, Blogger

def index(request):
    num_posts = Post.objects.all().count()
    num_bloggers = Blogger.objects.all().count()
    num_visits = request.session.get('num_visits', 0)
    num_visits += 1
    request.session['num_visits'] = num_visits

    context = {
        "num_posts": num_posts,
        "num_bloggers": num_bloggers,
        "num_visits": num_visits,
    }

    return render(request, 'index.html', context=context)

class PostListView(generic.ListView):
    model = Post
    paginate_by=5

class PostDetailView(generic.DetailView):
    model=Post
    ordering = ['-date']

class BloggerListView(generic.ListView):
    model=Blogger
    paginate_by=5

class BloggerDetailView(generic.DetailView):
    model=Blogger

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields = ['comment_text']
        labels = {'comment_text': 'Comment'}

    widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CommentCreateView(LoginRequiredMixin, CreateView):
    model=Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        post_id = self.kwargs['pk']
        form.instance.post = get_object_or_404(Post, pk=post_id)
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_id = self.kwargs['pk']
        context['post'] = get_object_or_404(Post, pk=post_id)
        return context
    
    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.kwargs['pk']})
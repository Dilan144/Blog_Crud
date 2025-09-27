from .models import Post
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView


class PostListView(ListView):
    model = Post
    template_name = "post-list.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "post-detail.html"

class PostCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ['title', 'body', 'author'] 
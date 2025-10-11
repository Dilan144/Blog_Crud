from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (CreateView,
                                       UpdateView, 
                                       DeleteView,
                                       )
from django.urls import reverse_lazy


class PostListView(ListView):
    model = Post
    template_name = "post-list.html"


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "post-detail.html"

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post 
    template_name = "post_new.html"
    fields = ['title', 'body', 'author'] 

class PostUpdateView(UpdateView):
       model = Post
       template_name = "post-update.html"
       fields = ['title', 'body']

class PostDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy('post-list')
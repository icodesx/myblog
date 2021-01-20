from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm

# Create your views here.


class IndexView(ListView):
    model = Post
    template_name = 'index.html'


class PostView(DetailView):
    model = Post
    template_name = 'post.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add-post.html'

from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, "blog/home.html", context)


def detail(request, slug):
    post = Post.objects.get(slug=slug)
    context = {
        "post": post
    }
    return render(request, "blog/detail.html", context)





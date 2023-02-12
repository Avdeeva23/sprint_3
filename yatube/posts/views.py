from django.conf import settings

from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Post, Group 


# Главная страница
def index(request):    
    posts = Post.objects.all()[:settings.NUMBER_POSTS]
    context = {
        "posts": posts,
    }
    return render(request, "posts/index.html", context) 

def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)[:settings.NUMBER_POSTS]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
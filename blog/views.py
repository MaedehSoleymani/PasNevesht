#pasnevesht Blog models

from django.shortcuts import render
from blog.models import Post

def home(request):
    posts=Post.objects.filter(status=1)
    context={'posts':posts}
    return render(request, 'blog/home.html', context)

def full_post(request,pid):
    posts=Post.objects.filter(status=1, id=pid)
    context={'posts':posts}
    return render(request,'blog/full_post.html',context)

from django.shortcuts import render, get_object_or_404
from .models import Blog


# Create your views here.


def blog_home(request):
    Blogs = Blog.objects.order_by('-date')
    return render(request, 'Blog/blog_home.html', {'Blogs': Blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'Blog/detail.html', {'blog': blog})

from django.shortcuts import render
from .models import BlogPost

# Create your views here.
def post_list(request):
    posts = BlogPost.objects.all()
    print(posts)
    return render(request=request, template_name='post.html', context={'posts': posts})


def post_detail(request, pk):
    post = BlogPost.objects.get(pk=pk)
    print(pk)
    return render(request=request, template_name='post_detail.html', context={'post': post})
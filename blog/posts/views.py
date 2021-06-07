from django.shortcuts import render
from .models import Post


# Create your views here.

def index(request):
    context = {'title': 'Clean Blog', 'posts': Post.objects.all()}
    return render(request, 'posts/index.html', context)


def post(request, id):
    post = Post.objects.get(id=id)
    context = {'title': f'Clean Blog - {post.title}', 'post': post}
    return render(request, 'posts/post.html', context)

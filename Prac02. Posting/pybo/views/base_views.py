from django.shortcuts import render

from ..models import Post

def index(request):
    context = {
        "post_list": Post.objects.all()
    }
    return render(request, 'pybo/post_list.html', context)

def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'pybo/post_detail.html', context)

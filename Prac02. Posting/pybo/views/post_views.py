from django.shortcuts import render, get_object_or_404, redirect
from ..forms import PostForm
from ..models import Post

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('pybo:index')
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'pybo/post_form.html', context)

def post_modify(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('pybo:detail', post_id=post.id)
    else:
        form = PostForm(instance=post)
    context = {'form': form,
               'post': post}
    return render(request, 'pybo/post_modify.html', context)

def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('pybo:index')

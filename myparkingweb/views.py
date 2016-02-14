from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post, AboutDetails
from myparkingweb.forms import PostForm


def feedback_list(request):
    posts = Post.objects.all().order_by('published_date')
    return render(request, 'myparkingweb/feedback_list.html', {'posts': posts})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return render(request, 'myparkingweb/post_edit.html', {'form': form,})
    else:
        form = PostForm()
    return render(request, 'myparkingweb/post_edit.html', {'form': form,})
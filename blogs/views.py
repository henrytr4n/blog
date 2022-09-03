from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import PostForm


def index(request):
    """The home page for Blog"""
    posts = BlogPost.objects.all()
    context = {"posts": posts}
    return render(request, "blogs/index.html", context)


def new_post(request):
    """Add a new post."""
    if request.method != "POST":
        # No data submitted; create a blank form.
        form = PostForm()
    else:
        # POST data submitted; process data.
        form = PostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("blogs:index")

    # Display a blank or invalid form.
    context = {"form": form}
    return render(request, "blogs/new_post.html", context)


def edit_post(request, post_id):
    """Edit an existing post."""
    post = BlogPost.objects.get(id=post_id)

    if request.method != "POST":
        # Initial request; pre-fill form with the current post.
        form = PostForm(instance=post)
    else:
        # POST data submitted; process data.
        form = PostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("blogs:index")

    context = {"post": post, "form": form}
    return render(request, "blogs/edit_post.html", context)

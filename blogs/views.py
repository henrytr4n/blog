from django.shortcuts import render
from .models import BlogPost
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
# def register(request):
#     form = UserCreationForm()
#     return render(request, "users/register.html", {"form": form})


def index(request):
    """The home page for Blog"""
    posts = BlogPost.objects.all()
    context = {"posts": posts}
    return render(request, "blogs/index.html", context)

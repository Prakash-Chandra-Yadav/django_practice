from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# NORMAL METHOD
# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, "post_list.html", {"posts": posts})

# LIST VIEW METHOD


class PostList(ListView):
    model = Post
    template_name = "post_list.html"


# Create your views here.

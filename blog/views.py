from django.shortcuts import redirect, render
from blog.forms import CommentForm
from blog.models import Post, Comment
# Create your views here.


def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts
    }
    return render(request, "blog_index.html", context)


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category).order_by('-created_on')
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    print(post, "AAAAAAAAAAAAAAAAAAAAAAAAa")
    comments = Comment.objects.filter(post=post)
    print(comments, "BBBBBBBBBBBBBBBBBBBBB")
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()
            return redirect("blog:blog_detail", pk=pk)
    context = {
        "post": post,
        "comments": comments,
        "form": form
    }
    return render(request, "blog_detail.html", context)

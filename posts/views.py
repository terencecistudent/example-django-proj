from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from .models import Post
from .forms import ForumPostForm, ForumCommentForm


def all_posts(request):
    """
    Return all of the posts and render
    them to all_posts.html
    """
    posts = Post.objects.filter(
        date_published__lte=timezone.now()).order_by('-date_published')
    return render(request, "all_posts.html", {'posts': posts})


def post_detail(request, pk):
    """
    Returns a single post based on the selected
    post ID and renders it to post_detail.html
    """
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    form = ForumCommentForm(request.POST)
    ctx = {"form": form}
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.user = request.user
        comment.save()
        messages.success(request,
                         "Comment has been posted successfully posted!")
        return redirect('post_detail', pk=post.id)
    return render(request, "post_detail.html", {'post': post}, ctx)


def create_or_edit_post(request, pk=None):
    """
    Create a view that allows us to create
    or edit a post depending if the Post ID
    is null or not
    """
    post = get_object_or_404(Post, pk=pk) if pk else None

    if post.user.username != request.user.username:
        return redirect("all_posts")
    else:
        if request.method == "POST":
            form = ForumPostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.user_id = request.user.id
                post = form.save()
                return redirect(post_detail, post.pk)
        else:
            form = ForumPostForm(instance=post)
    return render(request, "post_form.html", {"form": form})

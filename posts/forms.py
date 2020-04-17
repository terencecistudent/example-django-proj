from django import forms
from .models import Post, Comment


class ForumPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "content", "tag", )


class ForumCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content", )

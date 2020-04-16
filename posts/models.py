from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    """
    A single blog post
    """
    user = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_published = models.DateTimeField(
        default=timezone.now,
        blank=True,
        null=True
    )
    number_of_views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Comments in the post
    """
    post = models.ForeignKey(Post, related_name="comments")
    user = models.ForeignKey(User)
    content = models.TextField()
    comment_created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}-{}-{}".format(self.post.title, str(self.user.username),
                                    str(self.content))

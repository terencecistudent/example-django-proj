from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import Post


class TestPostsModel(TestCase):
    """
    Test posts title field as
    a string
    """
    def test_post_title_as_a_string(self):
        title = Post(title="Create a Test")
        self.assertEqual("Create a Test", str(title))

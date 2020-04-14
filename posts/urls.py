from django.conf.urls import url
from .views import all_posts, post_detail, create_post


urlpatterns = [
    url(r'all_posts', all_posts, name="all_posts"),
    url(r'^(?P<pk>\d+)/$', post_detail, name="post_detail"),
    url(r'^new/$', create_post, name="new_post"),
    # url(r'^add_comment/$', add_comment, name="add_comment"),
]

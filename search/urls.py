from django.conf.urls import url
from .views import search_for_a_book


urlpatterns = [
    url(r'^$', search_for_a_book, name="search")
]

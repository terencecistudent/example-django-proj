from django.conf.urls import url
from .views import all_of_the_books, book_info


urlpatterns = [
    url(r'^$', all_of_the_books, name="books"),
    url(r'^(?P<pk>\d+)/$', book_info, name="book_info"),
]

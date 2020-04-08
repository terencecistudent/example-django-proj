from django.conf.urls import url
from .views import all_of_the_books


urlpatterns = [
    url(r'^$', all_of_the_books, name="books"),
]

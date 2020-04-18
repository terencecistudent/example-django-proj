from django.conf.urls import url
from .views import all_of_the_books, book_info, comics, food, horror
from .views import mystery, sport, price_asc, price_desc, published_date_asc
from .views import published_date_desc


urlpatterns = [
    url(r'^$', all_of_the_books, name="books"),
    url(r'^(?P<pk>\d+)/$', book_info, name="book_info"),
    url(r'^comics$', comics, name="comics"),
    url(r'^food$', food, name="food"),
    url(r'^horror$', horror, name="horror"),
    url(r'^mystery$', mystery, name="mystery"),
    url(r'^sport$', sport, name="sport"),
    url(r'^price_asc$', price_asc, name="price_asc"),
    url(r'^price_desc$', price_desc, name="price_desc"),
    url(r'^published_date_asc$', published_date_asc,
        name="published_date_asc"),
    url(r'^published_date_desc$', published_date_desc,
        name="published_date_desc"),
]

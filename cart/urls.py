from django.conf.urls import url
from .views import view_cart, add_book_to_cart, edit_book_quantity, remove_item


urlpatterns = [
    url(r'^$', view_cart, name="view_cart"),
    url(r'add/(?P<id>\d+)', add_book_to_cart, name="add_book_to_cart"),
    url(r'edit/(?P<id>\d+)', edit_book_quantity, name="edit_book_quantity"),
    url(r'remove_item/(?P<id>\d+)', remove_item, name="remove_item"),
]

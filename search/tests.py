from django.test import TestCase
from books.models import Book


class TestSearchView(TestCase):
    """
    Test search a book
    """
    def test_search_a_book(self):
        book = Book(name="A book name")
        self.assertEqual("A book name", str(book))

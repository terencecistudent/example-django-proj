from django.test import TestCase
from .models import Book


class TestBookModel(TestCase):
    """
    Tests Book model
    """
    def test_book_as_a_string(self):
        book = Book(name="Create a Test")
        self.assertEqual("Create a Test", str(book))

    def test_book_as_a_int(self):
        book = Book(price=10)
        self.assertEqual(10, int("10"))


class TestBookView(TestCase):
    """
    Tests Book view
    """
    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")

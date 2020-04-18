from django.shortcuts import render, get_object_or_404
from .models import Book


def all_of_the_books(request):
    """
    A view that returns all of
    the books to the books.html page
    """
    books = Book.objects.all()
    return render(request, "books.html",
                  {"books": books})


def book_info(request, pk):
    """
    A view that returns information
    of a single book
    """
    book = get_object_or_404(Book, pk=pk)
    return render(request, "book_detail.html",
                  {"book": book})

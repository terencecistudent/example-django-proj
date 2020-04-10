from django.shortcuts import render
from .models import Book, Genre


def all_of_the_books(request):
    books = Book.objects.all()
    return render(request, "books.html",
                  {"books": books})


def book_info(request, book_id):
    book_information = Book.objects.filter(id=int(book_id))
    return render(request, "book_detail.html",
                  {"book_information": book_information})

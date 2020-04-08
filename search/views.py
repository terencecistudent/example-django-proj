from django.shortcuts import render
from books.models import Book


def search_for_a_book(request):
    books = Book.objects.filter(name__icontains=request.GET['q'])
    return render(request, "books.html", {"books": books})

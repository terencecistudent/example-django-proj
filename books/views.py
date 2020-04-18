from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Book


def all_of_the_books(request):
    """
    A view that returns all of
    the books to the books.html page
    """
    books = Book.objects.all()
    paginator = Paginator(books, 12)
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    return render(request, "books.html",
                  {"books": books})


def book_info(request, pk):
    """
    A view that returns information
    for a single book
    """
    book = get_object_or_404(Book, pk=pk)
    return render(request, "book_detail.html",
                  {"book": book})


def comics(request):
    books = Book.objects.filter(genre="Comics")
    paginator = Paginator(books, 12)
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    return render(request, "books.html",
                  {"books": books})


def food(request):
    books = Book.objects.filter(genre="Food")
    paginator = Paginator(books, 12)
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    return render(request, "books.html",
                  {"books": books})


def horror(request):
    books = Book.objects.filter(genre="Horror")
    paginator = Paginator(books, 12)
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    return render(request, "books.html",
                  {"books": books})


def mystery(request):
    books = Book.objects.filter(genre="Mystery")
    paginator = Paginator(books, 12)
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    return render(request, "books.html",
                  {"books": books})


def sport(request):
    books = Book.objects.filter(genre="Sport")
    paginator = Paginator(books, 12)
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    return render(request, "books.html",
                  {"books": books})


def price_asc(request):
    books = Book.objects.all().order_by("price")
    paginator = Paginator(books, 12)
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    return render(request, "books.html",
                  {"books": books})


def price_desc(request):
    books = Book.objects.all().order_by("-price")
    paginator = Paginator(books, 12)
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    return render(request, "books.html",
                  {"books": books})


def published_date_asc(request):
    books = Book.objects.all().order_by("published_date")
    paginator = Paginator(books, 12)
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    return render(request, "books.html",
                  {"books": books})


def published_date_desc(request):
    books = Book.objects.all().order_by("-published_date")
    paginator = Paginator(books, 12)
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    return render(request, "books.html",
                  {"books": books})

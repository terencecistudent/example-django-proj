from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from books.models import Book


def view_cart(request):
    """
    Renders everything within the cart,
    all of the items.
    """
    return render(request, "cart.html")


def add_book_to_cart(request, id):
    """
    For a specific book, add a
    quantity of it to the cart.
    """
    quantity = int(request.POST.get("quantity"))
    if quantity < 1:
        quantity = 1
        
    cart = request.session.get("cart", {})
    cart[id] = cart.get(id, quantity)
    request.session["cart"] = cart
    return redirect(reverse("books"))


def edit_book_quantity(request, id):
    """
    Adjust quantity of the specified book
    to the specific amount
    """
    quantity = int(request.POST.get("quantity"))
    cart = request.session.get("cart", {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session["cart"] = cart
    return redirect(reverse("view_cart"))


def remove_item(request, id):
    """
    Remove a book from the cart.
    """
    cart = request.session.get("cart", {})
    cart.pop(id)
    request.session["cart"] = cart
    messages.success(request, "Item removed from cart")
    return redirect(reverse("view_cart"))

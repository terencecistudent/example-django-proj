from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from books.models import Book
import stripe


stripe.api_key = settings.STRIPE_SECRET


@login_required
def checkout(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = PaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            cart = request.session.get("cart", {})
            total = 0

            for id, quantity in cart.items():
                book = get_object_or_404(Book, pk=id)
                total += quantity * book.price
                order_line_item = OrderLineItem(
                    order=order,
                    book=book,
                    quantity=quantity
                )
                order_line_item.save()

            try:
                customer_buying = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data["stripe_id"]
                )
            except stripe.error.CardError:
                messages.error(request, "Sorry your card has been denied!")

            if customer_buying.paid:
                messages.error(request, "Payment was successful!")
                request.session["cart"] = {}
                return redirect(reverse("books"))
            else:
                messages.error(request, "Payment was unsuccessful!")
        else:
            print(payment_form.errors)
            messages.error(
                request,
                "Sorry we were unable to process a payment with that card!"
            )
    else:
        payment_form = PaymentForm()
        order_form = OrderForm()

    return render(request, "checkout.html", {
        "order_form": order_form,
        "payment_form": payment_form,
        "publishable": settings.STRIPE_PUBLISHABLE
    })

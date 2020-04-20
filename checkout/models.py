from django.db import models
from books.models import Book
from django.contrib.auth.models import User


class Order(models.Model):
    """
    Fields used for when the user
    is checking out
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=40, blank=False)
    last_name = models.CharField(max_length=40, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=50, blank=False)
    street_address2 = models.CharField(max_length=50, blank=False)
    county = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}-{3}".format(self.id, self.date, self.first_name,
                                        self.last_name)


class OrderLineItem(models.Model):
    """
    Will return quantity of books being bought,
    book name and price.
    """
    order = models.ForeignKey(Order, null=False, related_name="orderline")
    book = models.ForeignKey(Book, null=False)
    quantity = models.IntegerField(blank=False)

    def line_total(self):
        return self.quantity * self.book.price

    def __str__(self):
        return "{0}-{1}-{2}".format(self.quantity, self.book.name,
                                    self.book.price)

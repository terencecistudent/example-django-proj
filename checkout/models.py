from django.db import models
from django.core.validators import RegexValidator
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
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex],
        max_length=15, blank=True)
    country = models.CharField(max_length=40, blank=False)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=50, blank=False)
    street_address2 = models.CharField(max_length=50, blank=True)
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

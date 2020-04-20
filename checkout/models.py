from django.db import models
from books.models import Book


class UserOrder(models.Model):
    """
    Fields used for when the user
    is checking out
    """
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
    order = models.ForeignKey(UserOrder, null=False)
    book = models.ForeignKey(Book, null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0}-{1}-{2}".format(self.quantity, self.book.name,
                                    self.book.price)

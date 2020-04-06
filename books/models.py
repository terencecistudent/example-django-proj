from django.db import models


class Book(models.Model):
    """
    Adding attributes to the fields for the Book model
    """
    name = models.CharField(max_length=100, default="")
    author = models.CharField(max_length=40, default="")
    description = models.TextField(max_length=200, default="")
    genre = models.CharField(max_length=40, default="")
    published_date = models.DateField(null=True, blank=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return self.name

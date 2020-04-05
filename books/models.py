from django.db import models


class Book(models.Model):
    """
    Adding attributes to the fields for the Book model
    """
    name = models.CharField(max_length=50, default="")
    author = models.CharField(max_length=40, default="")
    description = models.TextField(max_length=200, default="")
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return self.name

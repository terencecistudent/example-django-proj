from django.db import models


class Genre(models.Model):
    category = models.CharField(max_length=40, help_text="e.g. Fiction")

    def __str__(self):
        return self.category


class Author(models.Model):
    author_name = models.CharField(max_length=40, help_text="John Smith")

    def __str__(self):
        return self.author_name


class Book(models.Model):
    """
    Adding attributes to the fields for the Book model
    """
    name = models.CharField(max_length=100, default="")
    author = models.ManyToManyField(Author)
    description = models.TextField(max_length=250, default="")
    genre = models.ManyToManyField(Genre)
    published_date = models.DateField(null=True, blank=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return self.name

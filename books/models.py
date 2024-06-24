from django.db import models


class Book(models.Model):
    isbn = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    year_published = models.IntegerField()
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.title

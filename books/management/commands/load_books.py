import csv

from django.core.management.base import BaseCommand

from books.models import Book


class Command(BaseCommand):
    help = "Load books from a CSV file"

    def handle(self, *args, **kwargs):
        with open("books.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                Book.objects.create(
                    isbn=row["ISBN"],
                    title=row["Title"],
                    author=row["Author"],
                    year_published=row["Year Published"],
                    genre=row["Genre"],
                )
        self.stdout.write(self.style.SUCCESS("Data imported successfully"))

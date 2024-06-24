from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Book


class BookTests(APITestCase):
    def setUp(self):
        self.valid_data = {
            "isbn": "978-150-51423-879-1",
            "title": "The Divine Comedy",
            "author": "Leo Tolstoy",
            "year_published": 1903,
            "genre": "Poetry",
        }

    def test_create_book(self):
        url = reverse("book-list-create")
        response = self.client.post(url, self.valid_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_books(self):
        url = reverse("book-list-create")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_book(self):
        book = Book.objects.create(**self.valid_data)
        url = reverse("book-detail", args=[book.id])
        updated_data = self.valid_data.copy()
        updated_data["title"] = "The Divine Comedy - Updated"
        response = self.client.put(url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        book = Book.objects.create(**self.valid_data)
        url = reverse("book-detail", args=[book.id])
        response = self.client.delete(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

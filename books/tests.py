from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import AccessToken
from .models import Book


class BookAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = AccessToken.for_user(self.user)
        self.api_authentication()
        self.valid_data = {
            'isbn': '978-1234567890',
            'title': 'Test Book',
            'author': 'Test Author',
            'year_published': 2023,
            'genre': 'Test Genre'
        }

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_create_book_authenticated(self):
        url = '/api/books/'
        response = self.client.post(url, self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_books_authenticated(self):
        url = '/api/books/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

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

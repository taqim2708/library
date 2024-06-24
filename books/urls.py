from django.urls import path

from .views import BookDetail, BookListCreate

urlpatterns = [
    path("books/", BookListCreate.as_view(), name="book-list-create"),
    path("books/<int:pk>/", BookDetail.as_view(), name="book-detail"),
]

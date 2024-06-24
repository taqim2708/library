from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics

from .models import Book
from .serializers import BookSerializer


class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["author", "genre"]
    search_fields = ["title", "author", "genre"]
    ordering_fields = ["title", "year_published"]


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

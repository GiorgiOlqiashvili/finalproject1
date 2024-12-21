from rest_framework.viewsets import ModelViewSet
from .models import Book, Author, Genre, Condition, BookRequest
from .serializers import BookSerializer, AuthorSerializer, GenreSerializer, ConditionSerializer, BookRequestSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ConditionViewSet(ModelViewSet):
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer


class BookRequestViewSet(ModelViewSet):
    queryset = BookRequest.objects.all()
    serializer_class = BookRequestSerializer

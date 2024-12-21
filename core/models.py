from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Condition(models.Model):
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.status


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    condition = models.ForeignKey(Condition, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    location = models.CharField(max_length=255)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="owned_books")
    image = models.ImageField(upload_to='book_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class BookRequest(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='requests')
    requester = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_approved = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return f"{self.requester} requests {self.book}"


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    USERNAME_FIELD = 'email'  # Use email as the username field
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email

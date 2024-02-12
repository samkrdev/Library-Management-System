from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import uuid


# Create your models here.
class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)


class Author(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    CATEGORIES = [
        ("Self Development", "Self Development"),
        ("Business", "Business"),
        ("Engineering", "Engineering"),
        ("Science", "Science"),
        ("Technology", "Technology"),
        ("Management", "Management"),
        ("Fiction", "Fiction"),
        ("Non-Fiction", "Non-Fiction"),
        ("Magazines", "Magazines"),
    ]
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13, unique=True)
    total_count = models.IntegerField(default=0)
    available_count = models.IntegerField(default=0)
    load_count = models.IntegerField(default=0)
    categories = models.ManyToManyField(Category, help_text="Book Categories")

    def __str__(self):
        return self.title


class Issue(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "issued_books"

    def __str__(self):
        return f"{self.book.title} - {self.user.username}"


class Waitlist(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    added_date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "book")
        verbose_name_plural = "waitlist"

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"

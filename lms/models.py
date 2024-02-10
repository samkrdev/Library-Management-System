from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import uuid


# Create your models here.
class CustomUser(AbstractUser):
    pass


class Book(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    total_count = models.IntegerField(default=0)
    available_count = models.IntegerField(default=0)

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

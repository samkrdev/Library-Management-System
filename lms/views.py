from os import name
from django.shortcuts import render
from .models import Book


def book_list_view(request):
    books = Book.objects.all()
    return render(request, "books.html", {"books": books})

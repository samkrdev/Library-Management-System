# In a file named commands/generate_data.py
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from lms.models import Book, Issue, Waitlist
from faker import Faker


class Command(BaseCommand):
    help = "Create random books, issues, and waitlists"

    def add_arguments(self, parser):
        parser.add_argument(
            "total", type=int, help="Indicates the number of each model to be created"
        )

    def handle(self, *args, **kwargs):
        total = kwargs["total"]
        faker = Faker()
        User = get_user_model()

        superuser = User.objects.get(id=1)

        for _ in range(total):
            available_count = faker.random_int(min=0, max=100)
            Book.objects.create(
                title=faker.catch_phrase(),
                author=faker.name(),
                isbn=faker.isbn13(),
                total_count=available_count,
                available_count=available_count,
            )
            Issue.objects.create(
                user=superuser,
                book=Book.objects.order_by("?").first(),
                is_returned=faker.boolean(),
            )

        for book in Book.objects.filter(available_count=0):
            if not Waitlist.objects.filter(user=superuser, book=book).exists():
                Waitlist.objects.create(user=superuser, book=book)

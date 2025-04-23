# apps/bookmodule/management/commands/load_books.py
from django.core.management.base import BaseCommand
from apps.bookmodule.models import Book

class Command(BaseCommand):
    help = 'Loads sample books into database'

    def handle(self, *args, **options):
        books = [
            {
                "title": "The Hundred-Page Machine Learning Book", 
                "author": "Andriy Burkov",
                "price": 100.00,
                "edition": 4
            },
            # Add more books if needed
        ]
        
        for book_data in books:
            Book.objects.get_or_create(**book_data)
        
        self.stdout.write(self.style.SUCCESS(f'Successfully loaded {len(books)} books'))
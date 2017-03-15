# Django
from django.contrib import admin

# local Django
from .models import Author
from .models import Book
from .models import Publisher

admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)

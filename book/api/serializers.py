# third-party
from rest_framework import serializers

# local Django
from book.models import Author
from book.models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['book_id', 'title', 'price', 'author', 'publisher']
        # exclude = ['id', 'view_count']


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        # fields = ['book_id', 'title', 'price', 'author', 'publisher']
        exclude = ['id', 'view_count']

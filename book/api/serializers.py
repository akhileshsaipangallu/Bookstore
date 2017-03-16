# third-party
from rest_framework import serializers

# local Django
from book.models import Author
from book.models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['title']


class AuthorSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='author_full_name')
    books = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = ['name', 'books']

    @staticmethod
    def get_books(obj):
        book_list = Book.objects.filter(author=obj).order_by('-view_count')[:10]
        serializer = BookSerializer(book_list, many=True)
        return serializer.data

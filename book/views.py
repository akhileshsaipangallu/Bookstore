# Django
from django.shortcuts import get_object_or_404
from django.shortcuts import render

# local Django
from .models import Author
from .models import Book
from .models import Publisher


def home_page(request):
    context = {}
    return render(request, 'book/home_page.html', context)


def books(request):
    empty = False
    query_set = Book.objects.all()
    if not query_set:
        empty = True
    context = {
        'book_obj': query_set,
        'empty': empty,
    }
    return render(request, 'book/books.html', context)


def authors(request):
    empty = False
    query_set = Author.objects.all()
    if not query_set:
        empty = True
    context = {
        'author_obj': query_set,
        'empty': empty,
    }
    return render(request, 'book/authors.html', context)


def publishers(request):
    empty = False
    query_set = Publisher.objects.all()
    if not query_set:
        empty = True
    context = {
        'publisher_obj': query_set,
        'empty': empty,
    }
    return render(request, 'book/publishers.html', context)


def book_details(request, book_id):
    query_set = get_object_or_404(
        Book,
        book_id=book_id
    )
    context = {
        'book_obj': query_set,
    }
    query_set.author.view_count +=1
    query_set.author.save()
    query_set.view_count += 1
    query_set.save()
    return render(request, 'book/book_details.html', context)


def author_details(request, id):
    query_set = get_object_or_404(
        Author,
        id=id
    )
    context = {
        'author_obj': query_set,
    }
    return render(request, 'book/author_details.html', context)


def publisher_details(request, publisher_id):
    query_set = get_object_or_404(
        Publisher,
        publisher_id=publisher_id
    )
    context = {
        'publisher_obj': query_set,
    }
    return render(request, 'book/publisher_details.html', context)

# third-party
from rest_framework.decorators import api_view
from rest_framework.response import Response

# local Django
from book.models import Author
from .serializers import AuthorSerializer
from book.models import Book
from django.http import JsonResponse


def authors_top_ten(request):
    jason_data = []
    author_obj_top_ten = Author.objects.order_by('-view_count')[:10]
    for author_obj in author_obj_top_ten:
        author_dict = {}
        book_dict = {}
        book_obj_top_ten = \
            Book.objects.filter(author=author_obj).order_by('-view_count')[:10]
        temp_count = 0
        for book_obj in book_obj_top_ten:
            temp_count += 1
            book_dict['book %d' % temp_count] = book_obj.title
        author_dict[author_obj.first_name + ' ' + author_obj.last_name] = \
            book_dict
        jason_data.append(author_dict)

    return JsonResponse(jason_data, safe=False)


@api_view(['GET', 'POST'])
def authors_top_ten_rest(request):
    if request.method == 'GET':
        author_obj_top_ten = Author.objects.order_by('-view_count')[:10]
        author_serializer = AuthorSerializer(author_obj_top_ten, many=True)
        return Response(author_serializer.data)

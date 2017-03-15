# Django
from django.conf.urls import include
from django.conf.urls import url

# local Django
from . import views

urlpatterns = [
    url(r'^api/', include('book.api.urls')),
    url(r'^books/$', views.books, name='books'),
    url(r'^authors/$', views.authors, name='authors'),
    url(r'^publishers/$', views.publishers, name='publishers'),
    url(r'^books/(?P<book_id>\w+)$', views.book_details, name='book_details'),
    url(r'^authors/(?P<id>\w+)$', views.author_details, name='author_details'),
    url(
        r'^publishers/(?P<publisher_id>\w+)$',
        views.publisher_details,
        name='publisher_details'
    ),
]
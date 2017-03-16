# Django
from django.conf.urls import url

# local Django
import views


urlpatterns = [
    url(r'^authors/top10/$', views.authors_top_ten, name='authors_top_ten'),
    url(
        r'^authors/top10/rest/$',
        views.authors_top_ten_rest,
        name='authors_top_ten_rest'
    ),
]

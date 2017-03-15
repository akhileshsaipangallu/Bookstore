# Django
from django.conf.urls import url

# local Django
import views


urlpatterns = [
    url(r'^authors/top10/$', views.AuthorsTopTen.as_view(), name='books'),
    # url(
    #     r'^bank-(?P<ifsc>\w+)/$',
    #     views.BankDetails.as_view(),
    #     name='bank_details',
    # ),
]

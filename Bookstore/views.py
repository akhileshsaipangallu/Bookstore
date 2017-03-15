# Django
from django.shortcuts import render


def home_page(request):
    context = {}
    return render(request, 'book/home_page.html', context)

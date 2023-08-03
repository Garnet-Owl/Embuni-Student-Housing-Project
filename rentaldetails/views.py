from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Rental, BookRental, Book


def index(request):
    rentals = Rental.objects.all()[:5]
    return render(request, 'index.html', {'rentals': rentals})


def details(request):
    details2 = Rental.objects.all()[:15]
    # defining a dictionary.
    return render(request, 'details.html', {'details2': details2})


def about(request):
    about1 = Rental.objects.all()
    return render(request, 'about.html', {'about': about1})

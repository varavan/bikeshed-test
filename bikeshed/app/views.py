from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Bike
from app.forms import BikeForm


# Create your templates here.
def index(request):
    return render(
        request,
        'app/home.html')


@login_required
def add(request):
    form = BikeForm()

    return render(
        request,
        'app/add.html',
        {
            'form': form,
        })


def show(request, bikeid):
    bike = Bike.objects.get(pk=bikeid)

    # check if object does not exists

    return render(
        request,
        'app/show.html',
        {
            'bike': bike
        })

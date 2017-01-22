# coding=utf-8
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
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
    bike = get_object_or_404(Bike, pk=bikeid)

    return render(
        request,
        'app/show.html',
        {
            'bike': bike
        })
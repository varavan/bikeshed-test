from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Bike
from app.forms import BikeForm
from django.http import HttpResponse


# Create your templates here.
def index(request):
    bikes = Bike.objects.all().order_by('-id')[:50:1]

    return render(
        request,
        'app/home.html',
        {
            'bikes': bikes,
        })


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


def partial_add(request):
    if request.method == 'POST':
        form = BikeForm(request.POST, request.FILES)
        if form.is_valid():
            bike = form.save(commit=False)
            bike.created_by = request.user

            image = request.FILES['image']
            bike.image_thumbnail = image

            bike.save()
            # return 204 status as everything is okay and can continue
            return HttpResponse(status=204)

        return render(
            request,
            'app/partial/add_form.html',
            {
                'form': form
            }, status=400)

    else:
        return HttpResponse(status=405)
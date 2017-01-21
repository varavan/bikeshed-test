from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Bike
from app.forms import BikeForm


# Create your templates here.
def index(request):

    bikes = Bike.objects.all()

    return render(
        request,
        'app/home.html',
        {
            'bikes': bikes,
        }
    )

@login_required
def add(request):
    if request.method == 'POST':
        form = BikeForm(request.POST, request.FILES)
        if form.is_valid():
            bike = form.save(commit=False)
            image = request.FILES['image']
            bike.image_big = image
            bike.image_small = image
            bike.save()

            return redirect(index)
    else:
        form = BikeForm()
    return render(
            request,
            'app/add.html',
            {
                'form': form,
            }
        )

def show(request, bikeid):
    bike = Bike.objects.get(pk=bikeid)

    print('This is a test')
    print(bikeid)
    return render(
        request,
        'app/show.html',
        {
            'bike': bike
        }
    )

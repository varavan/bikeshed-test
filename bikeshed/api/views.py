from app.models import Bike
from app.forms import BikeForm
from .factories import bike_view_factory

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import JsonResponse


def list(request):
    bikes = [bike_view_factory(bike) for bike in Bike.objects.all().order_by('-price')[:50:1]]

    return JsonResponse(bikes, safe=False)


def list_sorted(request, sort, order):
    sortString = '-' if order == 'desc' else ''
    sortString += sort

    bikes = [bike_view_factory(bike) for bike in Bike.objects.all().order_by(sortString)[:50:1]]

    return JsonResponse(bikes, safe=False)


@login_required
def add(request):
    if request.method == 'POST':
        form = BikeForm(request.POST, request.FILES)
        if form.is_valid():
            bike = form.save(commit=False)
            bike.setImage(request.FILES['image'])
            bike.created_by = request.user

            bike.save()
            # return 204 status as everything is okay and can continue
            return JsonResponse({'redirect': reverse('index')})

        return JsonResponse(form.errors, status=400)

    else:
        return HttpResponse(status=405)

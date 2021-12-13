from django.shortcuts import render
from .models import Cities

# Create your views here.


def map(request):

    id = "1"

    cities = Cities.objects.all().filter(id = id)

    context = {'cities': cities}
    return render(request, 'MapApp/map.html', context)

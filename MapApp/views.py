from django.shortcuts import render
from .models import Cities, Event

# Create your views here.


def map(request, id):

    # FILTER CITIES BY 'ID' ( DATABASE_ATTRIBUTE - PARAMETER )
    cities = Cities.objects.filter(id=id)

    # FILTER EVENTS BY 'ID' ( DATABASE_ATTRIBUTE - PARAMETER )
    events = Event.objects.filter(citie=id)

    context = {'cities': cities, 'events': events}
    return render(request, 'MapApp/map.html', context)


def default(request):
    # FILTER CITIES BY 'ID' ( DATABASE_ATTRIBUTE - PARAMETER )
    cities = Cities.objects.filter(id=1)

    # FILTER EVENTS BY 'ID' ( DATABASE_ATTRIBUTE - PARAMETER )
    events = Event.objects.filter(citie=1)

    context = {'cities': cities, 'events': events}
    return render(request, 'MapApp/map.html', context)

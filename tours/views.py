from django.shortcuts import render
from .models import Continent, Tour
from django.views.generic import ListView

def continents(request):
    """Returns the continents page"""

    continents = Continent.objects.all()
    context = {
        'continents': continents
    }
    
    return render(request, 'tours/continents.html', context)


def tours(request):
    """Returns the tours page for each requested continent"""
    
    tours = Tour.objects.all()
    continent = None


    if request.GET:
        if 'continent' in request.GET:
            continent = request.GET['continent'].split(',')
            tours = tours.filter(continent__continent__in=continent)
            continent = Continent.objects.filter(continent__in=continent)

    context = {
        'current_continent': continent,
        'tours': tours
    }
        
    return render(request, 'tours/tours.html', context)
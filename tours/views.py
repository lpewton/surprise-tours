from django.shortcuts import render, get_object_or_404
from .models import Continent, Tour

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


def tour_detail(request, tour_id):
    """Returns the detailed tour page"""

    tour = get_object_or_404(Tour, pk=tour_id)

    context = {
        'tour': tour,
    }

    return render(request, 'tours/tour_detail.html', context)
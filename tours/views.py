from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from django.db.models.functions import Lower

from .models import Continent, Tour
from .forms import TourForm

def continents(request):
    """Returns the continents page"""

    continents = Continent.objects.all()
    context = {
        'continents': continents
    }

    return render(request, 'tours/continents.html', context)


def tours(request):
    """Returns the tours page for each requested continent and search/sort functionality"""

    tours = Tour.objects.all()
    continent = None
    sort = None
    direction = None

    if request.GET:
        if 'continent' in request.GET:
            continent = request.GET['continent'].split(',')
            tours = tours.filter(continent__continent__in=continent)
            continent = Continent.objects.filter(continent__in=continent)

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'location':
                sortkey = 'lower_location'
                tours = tours.annotate(lower_location=Lower('location'))
            if sortkey == 'continent':
                sortkey = 'continent__name'
            
            tours = tours.order_by(sortkey)

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            tours = tours.order_by(sortkey)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a destination or date!")
                return redirect(reverse('tours'))
            
            queries = Q(name__icontains=query) | Q(location__icontains=query) | Q(start__icontains=query) | Q(end__icontains=query)
            tours = tours.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'current_continent': continent,
        'tours': tours,
        'current_sorting': current_sorting,
    }

    return render(request, 'tours/tours.html', context)


def tour_detail(request, tour_id):
    """Returns the detailed tour page"""

    tour = get_object_or_404(Tour, pk=tour_id)

    context = {
        'tour': tour,
    }

    return render(request, 'tours/tour_detail.html', context)

def add_tour(request):
    form = TourForm()
    context = {
        'form': form
    }

    if request.method == 'POST':
        form = TourForm(request.POST, request.FILES)
        if form.is_valid():
            tour = form.save()
            messages.success(request, 'Tour added correctly')
            return redirect(reverse('tour_detail', args=[tour.id]))
        else:
            error_message = form.errors.as_text()
            messages.error(request, error_message)
            return redirect('add_tour')

    return render(request, 'tours/add_tour.html', context)

def remove_tour(request, tour_id):
    tour = get_object_or_404(Tour, pk=tour_id)

    tour.delete()
    
    return redirect('tours')



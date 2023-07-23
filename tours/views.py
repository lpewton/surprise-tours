from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from django.db.models.functions import Lower
from django.utils import timezone

from .models import Continent, Tour
from .forms import TourForm
from profiles.models import Review


def continents(request):
    """
    Returns the continents page
    """
    continents = Continent.objects.all()

    context = {
        'continents': continents
    }

    return render(request, 'tours/continents.html', context)


def tours(request):
    """
    Returns the tours page for each requested
    continent and search/sort functionality
    """
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
            if sortkey == 'meeting_location':
                sortkey = 'lower_meeting_location'
                tours = tours.annotate(
                    lower_meeting_location=Lower('meeting_location'))
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

            queries = Q(name__icontains=query) | Q(
                meeting_location__icontains=query) | Q(
                    description__icontains=query)

            tours = tours.filter(queries)

            context = {
                'q': query,
            }

    current_sorting = f'{sort}_{direction}'

    context = {
        'current_continent': continent,
        'tours': tours,
        'current_sorting': current_sorting,
    }

    return render(request, 'tours/tours.html', context)


def tour_detail(request, tour_id):
    """
    Returns the detailed tour page
    """
    tour = get_object_or_404(Tour, pk=tour_id)
    reviews = Review.objects.all()

    context = {
        'tour': tour,
        'reviews': reviews,
    }

    return render(request, 'tours/tour_detail.html', context)


def add_tour(request):
    """
    Allows admin to add a new tour
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')

        return redirect(reverse('home'))

    form = TourForm()
    context = {
        'form': form
    }

    if request.method == 'POST':
        form = TourForm(request.POST, request.FILES)

        if form.is_valid():
            start_date = form.cleaned_data['start']
            end_date = form.cleaned_data['end']
            slots = form.cleaned_data['slots']
            slots_left = form.cleaned_data['slots_left']

            if start_date <= timezone.now().date():
                messages.error(request, 'Start date must be later than today!')
            elif end_date <= start_date:
                messages.error(request, 'End date cannot be sooner'
                                        'than start date!')
            elif slots_left > slots:
                messages.error(
                    request, 'There are more slots left than slots available!')
            else:
                tour = form.save()
                messages.success(request, 'Tour added correctly')

                return redirect(reverse('tour_detail', args=[tour.id]))

        else:
            error_message1 = form.errors.as_text().split('*')[1].title()
            error_message2 = form.errors.as_text().split('*')[2]
            messages.error(request, f'{error_message1}: {error_message2}')

            return redirect('add_tour')

    return render(request, 'tours/add_tour.html', context)


def remove_tour(request, tour_id):
    """
    Remove one of the tours
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')

        return redirect(reverse('home'))

    tour = get_object_or_404(Tour, pk=tour_id)

    tour.delete()

    return redirect('tours')


def edit_tour(request, tour_id):
    """
    Edit one of the tours
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')

        return redirect(reverse('home'))

    tour = get_object_or_404(Tour, pk=tour_id)
    form = TourForm(instance=tour)

    context = {
        'form': form,
        'tour': tour,
    }

    if request.method == 'GET':

        return render(request, 'tours/edit_tour.html', context)

    if request.method == 'POST':
        form = TourForm(request.POST, request.FILES, instance=tour)

        if form.is_valid():
            start_date = form.cleaned_data['start']
            end_date = form.cleaned_data['end']
            slots = form.cleaned_data['slots']
            slots_left = form.cleaned_data['slots_left']

            if start_date <= timezone.now().date():
                messages.error(request, 'Start date must be later than today!')
            elif end_date <= start_date:
                messages.error(request, 'End date cannot be sooner'
                                        'than start date!')
            else:
                if slots_left > slots:
                    messages.error(
                        request, 'There are more slots left'
                                 'than slots available!')
                else:
                    tour = form.save()
                    messages.success(request, 'Tour edited correctly')

                    return redirect(reverse('tour_detail', args=[tour.id]))

            return render(request, 'tours/edit_tour.html', context)

        else:
            error_message1 = form.errors.as_text().split('*')[1].title()
            error_message2 = form.errors.as_text().split('*')[2]
            messages.error(request, f'{error_message1}: {error_message2}')

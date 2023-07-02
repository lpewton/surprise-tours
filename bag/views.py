from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils import timezone

from tours.models import Tour
from .contexts import *


def bag(request):
    """Returns the bag page"""

    return render(request, 'bag/bag.html')


def add_to_bag(request, tour_id):
    """Add a product and its quantity to the bag"""
    tour = get_object_or_404(Tour, pk=tour_id)
    quantity = int(request.POST.get('tour_quantity'))
    bag = request.session.get('bag', {})

    if tour_id in list(bag.keys()):
        bag[tour_id] += quantity    
        messages.success(request, f'Added {tour.name} to your bag')
    else:
        bag[tour_id] = quantity    
        messages.success(request, f'Added {tour.name} to your bag')
    
    tour.slots_left -= quantity
    tour.save()
    request.session['bag'] = bag

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove_from_bag(request, tour_id):
    """ Removes product from bag completely"""
    tour = get_object_or_404(Tour, pk=tour_id)
    bag_items = request.session['bag']

    for bag_tour, quantity in bag_items.items():
        if int(bag_tour) == int(tour.id):
            tour.slots_left += quantity
            tour.save()

    del bag_items[tour_id]
    request.session['bag'] = bag_items

    return redirect('bag')


def addPassenger(request, tour_id):
    """ Adds a passenger to the specific tour within the bag"""
    tour = get_object_or_404(Tour, pk=tour_id)
    bag_items = request.session['bag']
    for bag_tour, quantity in bag_items.items():
        if int(bag_tour) == int(tour.id):
            if tour.slots_left > quantity:
                quantity += 1
                bag_items[bag_tour] = quantity
            else:
                messages.error(request, "Sorry, there's no more space in this tour")

    request.session['bag'] = bag_items

    return redirect('bag')


def removePassenger(request, tour_id):
    """ Removes a passenger to the specific tour within the bag"""
    tour = get_object_or_404(Tour, pk=tour_id)
    bag_items = request.session['bag']
    for bag_tour, quantity in bag_items.items():
        if int(bag_tour) == int(tour.id):
            if quantity > 1:
                quantity -= 1
                bag_items[bag_tour] = quantity
            else:
                messages.error(request, "Please remove the tour from your bag if you no longer want to purchase it")
    request.session['bag'] = bag_items

    return redirect('bag')
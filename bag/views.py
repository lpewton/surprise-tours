from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect

from tours.models import Tour
from .contexts import *

def add_to_bag(request, tour_id):
    """Add a product and it's quantity to the bag"""

    tour = get_object_or_404(Tour, pk=tour_id)
    quantity = int(request.POST.get('tour_quantity'))
    bag = request.session.get('bag', {})

    if tour_id in list(bag.keys()):
        bag[tour_id] += quantity    
        messages.success(request, (f'Added {tour.name} to your bag'))
    else:
        bag[tour_id] = quantity    
        messages.success(request, (f'Added {tour.name} to your bag'))
    
    tour.slots_left -= quantity
    tour.save()
    request.session['bag'] = bag

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def bag(request):
    """Returns the bag page"""

    return render(request, 'bag/bag.html') 
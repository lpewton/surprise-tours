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
    expiry_time = calculateExpiryTime(request)

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

def calculateExpiryTime(request):
    
    cookieAge = 30 #How many seconds it takes for session to expire
    timeNow = timezone.now()
    expiryTime = cookieAge + int(timeNow.timestamp())

    print(expiryTime)

    return expiryTime
    
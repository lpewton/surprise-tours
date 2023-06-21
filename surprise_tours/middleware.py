from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils import timezone

from bag.views import *

class ExpiredItemsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # calculate expiryTime only if 'bag'session exists
        if 'bag' in request.session and 'expiryTime' not in request.session:
            request.session['expiryTime'] = calculateExpiryTime(request)

        response = self.get_response(request)
        
        self.clear_bag(request)
        
        return response

    def clear_bag(self, request):
        if 'bag' in request.session and request.session['bag']:
            time_now = int(timezone.now().timestamp())
            
            if 'expiryTime' in request.session:
                expiryTime = request.session['expiryTime']
                warningTime = int(expiryTime) - 20

            else:
                expiryTime = None
                warningTime = None
            

            if warningTime and time_now >= warningTime:
                messages.warning(request, "Session is about to expire! Please hurry and buy")


            if expiryTime and time_now >= expiryTime:
                messages.error(request, "Session expired")

                # Reset bag and expiry date session
                del request.session['bag']
                del request.session['expiryTime']

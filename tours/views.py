from django.shortcuts import render
from .models import Continent
from django.views.generic import ListView

def continents(request):
    """Returns the continents page"""

    continents = Continent.objects.all()
    context = {
        'continents': continents
    }
    
    return render(request, 'tours/continents.html', context)
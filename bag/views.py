from django.shortcuts import render

def bag(request):
    """Returns the bag page"""

    return render(request, 'bag/bag.html') 
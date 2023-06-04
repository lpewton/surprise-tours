from django.shortcuts import render

def continents(request):
    """Returns the index page"""
    return render(request, 'tours/continents.html') 
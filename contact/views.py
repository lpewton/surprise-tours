from django.shortcuts import render


def contact(request):
    """Returns the contact page"""

    return render(request, 'contact/contact.html') 
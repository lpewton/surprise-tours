from django.shortcuts import render

from .forms import contactForm


def contact(request):
    """Returns the contact page"""
    form = contactForm()

    context = {
        'form': form
    }

    return render(request, 'contact/contact.html', context) 
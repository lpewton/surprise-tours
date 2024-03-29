from django.shortcuts import render
from django.contrib import messages

from .forms import messageForm


def contact(request):
    """
    Returns the contact page
    """
    form = messageForm()

    if request.method == 'POST':
        message_form = form(request.POST)
        if message_form.is_valid():
            message_form.save()
            messages.success(request, "Message sent!")

        else:
            messages.error(
                request, "Message couldn't be sent, please try again later")

    context = {
        'form': form
    }

    return render(request, 'contact/contact.html', context)


def newsletter(request):
    """
    Returns the subscribe to newsletter page
    """

    return render(request, 'contact/newsletter.html')

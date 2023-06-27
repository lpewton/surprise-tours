from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    if request.method == 'GET':
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('tours'))
        else:
            form = OrderForm
            context = {
                'form': form
            }
            return render(request, 'checkout/checkout.html', context)


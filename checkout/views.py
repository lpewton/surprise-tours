from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from django.views.decorators.http import require_POST

from.models import Order, OrderItem
from tours.models import Tour
from .forms import OrderForm
from bag.contexts import bag_contents

import stripe

@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return render(request, 'checkout/checkout.html')
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return render(request, 'checkout/checkout.html')


def checkout(request):
    if request.method == 'POST':

        bag = request.session.get('bag', {})
        
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'nationality': request.POST['nationality'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        order_form = OrderForm(form_data)

        if order_form.is_valid:
            order = order_form.save()
            for item_id, item_quantity in bag.items():
                try:
                    tour = Tour.objects.get(id=item_id)
                    order_item = OrderItem(
                        order=order,
                        tour=tour,
                        quantity=item_quantity,
                    )
                    order_item.save()
                    
                except Tour.DoesNotExist:
                    messages.error(request, (
                        "One of the tours is not available anymore! Order cancelled!")
                    )
                    order.delete()
                    return redirect(reverse('bag'))
        
        else:
            messages.error(request, "Something went wrong")
        return render(request, 'checkout/checkout.html')



    if request.method == 'GET':
        stripe_public_key = settings.STRIPE_PUBLIC_KEY
        stripe_secret_key = settings.STRIPE_SECRET_KEY
        bag = request.session.get('bag', {})
        current_bag = bag_contents(request)
        total = current_bag['total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if not bag:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('tours'))
        else:
            form = OrderForm
            context = {
                'form': form,
                'stripe_public_key': stripe_public_key,
                'client_secret': intent.client_secret,
            }
            return render(request, 'checkout/checkout.html', context)

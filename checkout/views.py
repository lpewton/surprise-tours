from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.views.decorators.http import require_POST

from.models import Order, OrderItem
from tours.models import Tour
from profiles.models import UserProfile
from .forms import OrderForm
from bag.contexts import bag_contents

import stripe
import json

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
        if request.user.is_authenticated:
            profile = get_object_or_404(UserProfile, user=request.user)

        if order_form.is_valid:
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            if request.user.is_authenticated:
                order.user_profile = profile
            order.save()            
            for item_id, item_quantity in bag.items():
                try:
                    tour = Tour.objects.get(id=item_id)
                    order_item = OrderItem(
                        order=order,
                        tour=tour,
                        quantity=item_quantity,
                    )
                    order_item.save()
                    
                    return redirect(reverse('checkout_success', args=[order.order_number]))

                    
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
            if request.user.is_authenticated:
                profile = UserProfile.objects.get(user=request.user)
                form = OrderForm(initial={
                        'full_name': profile.user.get_full_name(),
                        'email': profile.user.email,
                        'phone_number': profile.profile_phone_number,
                        'country': profile.profile_country,
                        'postcode': profile.profile_postcode,
                        'town_or_city': profile.profile_town_or_city,
                        'street_address1': profile.profile_street_address1,
                        'street_address2': profile.profile_street_address2,
                        'county': profile.profile_county,
                    })    
            else:
                form = OrderForm()         
            context = {
                'form': form,
                'stripe_public_key': stripe_public_key,
                'client_secret': intent.client_secret,
            }
            return render(request, 'checkout/checkout.html', context)

def checkoutSuccess(request, order_number):
    """ Rendered after order is successful """
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Pack your bags! Your order has been successful')

    if 'bag' in request.session:
        del request.session['bag']

    context = {
        'order': order
    }
    return render(request, 'checkout/checkout-success.html', context) 
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, OrderItem
from tours.models import Tour

import stripe
import json
import time


class StripeWH_Handler:
    """
    Handle Stripe webhooks
    """

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """
        Send the user a confirmation email
        """

        cust_email = order.email

        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})

        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """

        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """

        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info
        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )
        billing_details = stripe_charge.billing_details
        order_total = round(stripe_charge.amount / 100, 2)

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=billing_details.name,
                    phone_number__iexact=billing_details.phone,
                    email__iexact=billing_details.email,
                    street_address1__iexact=billing_details.address.line1,
                    street_address2__iexact=billing_details.address.line2,
                    town_or_city__iexact=billing_details.address.city,
                    country__iexact=billing_details.address.country,
                    county__iexact=billing_details.address.state,
                    order_total=order_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break

            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if order_exists:
            self._send_confirmation_email(order)

            return HttpResponse(
                content=f'Webhook received: {event["type"]} | '
                        'SUCCESS: Verified order already in database',
                status=200)

        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=billing_details.name,
                    email=billing_details.email,
                    phone_number=billing_details.phone,
                    country=billing_details.address.country,
                    town_or_city=billing_details.address.city,
                    street_address1=billing_details.address.line1,
                    street_address2=billing_details.address.line2,
                    county=billing_details.address.state,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(bag).items():
                    tour = Tour.objects.get(id=item_id)
                    order_item = OrderItem(
                        order=order,
                        tour=tour,
                        quantity=item_data,
                    )
                    order_item.save()

            except Exception as e:
                if order:
                    order.delete()

                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR',
                    status=500)

        self._send_confirmation_email(order)

        return HttpResponse(
            content=f'Webhook received: {event["type"]} | '
                    'SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

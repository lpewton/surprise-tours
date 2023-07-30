import uuid

from django.db import models
from django.db.models import Sum
from django_countries.fields import CountryField

from tours.models import Tour
from profiles.models import UserProfile


class Order(models.Model):
    """
    Saves order details during purchase
    """
    order_number = models.CharField(max_length=30, null=False, editable=False)
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=False, blank=False)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=False, blank=False)
    county = models.CharField(max_length=80, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    show_date = models.DateField(auto_now_add=True)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        """
        Generate a random order number using UUID
        """
        return uuid.uuid4().hex.upper()[:30]

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        only if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def update_total(self):
        """
        Update grand total each time a line item is added.
        """
        self.order_total = self.lineitems.aggregate(
            total=Sum('item_total'))['total'] or 0
        self.save()

    def upon_arrival(self):
        return self.order_total * 9

    def __str__(self):
        return self.order_number

    class Meta:
        ordering = ["-date"]


class OrderItem(models.Model):
    """
    Saves each tour within the total purchase
    """
    order = models.ForeignKey(
        Order, null=False, blank=False, on_delete=models.CASCADE,
        related_name='lineitems')
    tour = models.ForeignKey(
        Tour, null=False, blank=False, on_delete=models.SET(61))
    quantity = models.IntegerField(null=False, blank=False, default=0)
    item_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False,
        blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the item total
        and then update the order total.
        """
        self.item_total = self.tour.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.tour} tour on order {self.order.order_number}'

from django.contrib import admin

from .models import Order, OrderItem


class OrderItemAdminInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('item_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemAdminInline,)

    readonly_fields = ('order_number', 'date', 'user_profile',
                       'order_total', 'original_bag', 'stripe_pid')

    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country', 'user_profile',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county',
              'order_total', 'original_bag', 'stripe_pid')

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'user_profile')

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)

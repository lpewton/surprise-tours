from django.contrib import admin

from .models import message


class messageAdmin(admin.ModelAdmin):
    model = message
    list_display = (
        'full_name', 'subject'
    )

admin.site.register(message, messageAdmin)
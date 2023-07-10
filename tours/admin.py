from django.contrib import admin
from .models import Continent, Tour

class ContinentAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
    )

class TourAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'meeting_location', 'start', 'end', 'continent',
    )

admin.site.register(Continent, ContinentAdmin)
admin.site.register(Tour, TourAdmin)


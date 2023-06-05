from django.contrib import admin
from .models import Continent, Tour

class ContinentAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
    )

class TourAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'location', 'start_date', 'end_date', 'continent',
    )

admin.site.register(Continent, ContinentAdmin)
admin.site.register(Tour, TourAdmin)


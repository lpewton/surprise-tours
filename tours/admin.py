from django.contrib import admin
from .models import Continent

class ContinentAdmin(admin.ModelAdmin):
    list_display = (
        'continent',
    )

admin.site.register(Continent, ContinentAdmin)


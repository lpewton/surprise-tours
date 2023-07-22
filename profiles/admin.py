from django.contrib import admin

from .models import UserProfile, review


class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    list_display = (
        'user',
    )


class reviewAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'tour', 'rating', 'review', 'date',
    )


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(review, reviewAdmin)

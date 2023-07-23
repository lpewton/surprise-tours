from django.contrib import admin

from .models import UserProfile, Review


class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    list_display = (
        'user',
    )


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'tour', 'rating', 'review', 'date', 'approved',
    )


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Review, ReviewAdmin)

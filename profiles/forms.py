from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_full_name', 'profile_email',
                  'profile_phone_number', 'profile_nationality',
                  'profile_street_address1', 'profile_street_address2',
                  'profile_town_or_city', 'profile_postcode',
                  'profile_country', 'profile_county',)

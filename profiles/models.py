from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField
from django.core.validators import MinValueValidator, MaxValueValidator

from tours.models import Tour


class UserProfile(models.Model):
    """
    Stores user's information
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_full_name = models.CharField(
        max_length=50, null=False, blank=False)
    profile_email = models.EmailField(max_length=254, null=False, blank=False)
    profile_phone_number = models.CharField(
        max_length=20, null=False, blank=False)
    profile_nationality = CountryField(
        blank_label='Nationality *', null=False, blank=False)
    profile_country = CountryField(
        blank_label='Country *', null=False, blank=False)
    profile_postcode = models.CharField(max_length=20, null=True, blank=True)
    profile_town_or_city = models.CharField(
        max_length=40, null=False, blank=False)
    profile_street_address1 = models.CharField(
        max_length=80, null=False, blank=False)
    profile_street_address2 = models.CharField(
        max_length=80, null=True, blank=True)
    profile_county = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return self.profile_full_name


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Creates or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()


class Review(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    rating = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(10)], default=0)
    review = models.CharField(
        max_length=150, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)

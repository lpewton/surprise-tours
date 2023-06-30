from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyProfile, name='my_profile'),
]
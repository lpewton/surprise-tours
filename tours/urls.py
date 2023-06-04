from django.urls import path
from . import views

urlpatterns = [
    path('continents/', views.continents, name='continents'),
]
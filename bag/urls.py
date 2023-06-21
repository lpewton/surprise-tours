from django.urls import path
from . import views

urlpatterns = [
    path('bag/', views.bag, name='bag'),
    path('add/<tour_id>/', views.add_to_bag, name='add_to_bag'),
    path('bag/remove/<tour_id>/', views.remove_from_bag, name='remove_from_bag'),]
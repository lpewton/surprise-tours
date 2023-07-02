from django.urls import path
from . import views

urlpatterns = [
    path('bag/', views.bag, name='bag'),
    path('add/<tour_id>/', views.add_to_bag, name='add_to_bag'),
    path('add_passenger/<int:tour_id>', views.addPassenger, name='add_passenger'),
    path('remove_passenger/<int:tour_id>', views.removePassenger, name='remove_passenger'),
    path('bag/remove/<tour_id>/', views.remove_from_bag, name='remove_from_bag'),]
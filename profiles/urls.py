from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyProfile, name='my_profile'),
    path('past_orders', views.pastOrders, name='past_orders'),
]
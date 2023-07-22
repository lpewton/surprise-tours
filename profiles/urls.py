from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyProfile, name='my_profile'),
    path('past_orders', views.pastOrders, name='past_orders'),
    path('<int:order_id>/', views.orderDetail, name='order_detail'),
]

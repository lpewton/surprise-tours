from django.urls import path
from . import views

urlpatterns = [
    path('continents/', views.continents, name='continents'),
    path('tours/', views.tours, name='tours'),
    path('<int:tour_id>/', views.tour_detail, name='tour_detail'),
    path('add_tour/', views.add_tour, name='add_tour'),
    path('remove_tour/<int:tour_id>', views.remove_tour, name='remove_tour'),
    path('edit_tour/<int:tour_id>', views.edit_tour, name='edit_tour'),
]
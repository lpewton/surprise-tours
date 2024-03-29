from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyProfile, name='my_profile'),
    path('past_orders', views.pastOrders, name='past_orders'),
    path('<int:order_id>/', views.orderDetail, name='order_detail'),
    path('review/', views.review, name='review'),
    path('pending-reviews/', views.pendingReviews, name='pending_reviews'),
    path('approve-review/<int:review_id>',
         views.approveReview, name='approve_review'),
    path('reject-review/<int:review_id>',
         views.rejectReview, name='reject_review'),
]

from django.urls import path

from restaurant.views import RestaurantListView,  RestaurantDetailView 


app_name = 'restaurant'

urlpatterns = [
    path('', RestaurantListView.as_view(), name="index"),
    path('<int:pk>', RestaurantDetailView.as_view(), name="detail"),
]
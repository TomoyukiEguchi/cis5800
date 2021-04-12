
from django.urls import path
from staffroom.views import RestaurantCreateView, RestaurantUpdateView, RestaurantDeleteView

app_name = "restaurant"

urlpatterns = [
    path('create', RestaurantCreateView.as_view(), name="create"),
    path('<int:pk>/update', RestaurantUpdateView.as_view(), name="update"),
    path('<int:pk>/delete', RestaurantDeleteView.as_view(), name="delete"),
]
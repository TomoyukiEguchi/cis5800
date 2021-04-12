from django.urls import path, include
from ..views import StaffroomTemplateView


app_name = "staffroom"

urlpatterns = [
    path("", StaffroomTemplateView.as_view(), name="index"),
    path("restaurant/", include("staffroom.urls.restaurant", namespace="restaurant")),
]
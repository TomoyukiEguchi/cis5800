from django import forms

from .models import Restaurant


class RestaurantForm(forms.ModelForm):

    class Meta:
        model = Restaurant
        fields = ['name', 'area', 'cuisine', 'live_capacity', 'address1', 'address2', 'city', 'state', 'zipcode', "user", ]

        widgets = {
            "user": forms.HiddenInput()
        }

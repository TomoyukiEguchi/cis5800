from django import forms

from .models import Restaurant


class RestaurantForm(forms.ModelForm):

    class Meta:
        model = Restaurant
        fields = ['name', 'area', 'cuisine', 'live_capacity', 'address1', 'address2', 'city', 'state', 'zipcode', "user", ]

        widgets = {
            "user": forms.HiddenInput()
        }


class SearchForm(forms.Form):
    q = forms.CharField(min_length=1, max_length=20, label='', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


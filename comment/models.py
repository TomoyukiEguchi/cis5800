from django.db import models
from restaurant.models import Restaurant
from phone_field import PhoneField



# Create your models here.

class Comment(models.Model):

    full_name = models.CharField(max_length=50)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    email = models.EmailField(max_length=254)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, default=None, null=True)
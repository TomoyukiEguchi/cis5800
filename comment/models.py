from django.db import models
from restaurant.models import Restaurant

# Create your models here.
class Comment(models.Model):

    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, default=None, null=True)
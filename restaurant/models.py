from django.db import models

from django.contrib.auth.models import User


# Create your models here.

cuisine_choice = (
    ('', 'Choose...'),
    ('American', 'American'),
    ('European', 'European'),
    ('French', 'French'),
    ('Mexican', 'Mexican'),
    ('Italian', 'Italian'),
    ('Japanese', 'Japanese'),
    ('Middle Eastern', 'Middle Eastern'),
    ('Latin', 'Latin American'),
)

capacity_choice = (
    ('', 'Choose...'),
    ('100', '100'),
    ('75', '75'),
    ('50', '50'),
    ('25', '25'),
    ('10', '10'),
)

state = (
    ('', 'Choose...'),
    ('CA', 'California'),
    ('NY', 'New York'),
    ('IL', 'Chicago')
)

class Restaurant(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    area = models.CharField(max_length=50, blank=True, null=True)
    cuisine = models.CharField(max_length=50, blank=True, null=True, choices=cuisine_choice)
    live_capacity = models.CharField(max_length=50, blank=True, null=True, choices=capacity_choice)
    address1 = models.CharField(max_length=50, blank=True, null=True)
    address2 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True, choices=state)
    zipcode = models.CharField(max_length=50, blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
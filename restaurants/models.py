from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Restaurant(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('closed', 'Closed'),
    ]
    
    name = models.CharField(max_length=255)
    address = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='restaurants')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open')

    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/', null=True, blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menus')

    def __str__(self):
        return self.name

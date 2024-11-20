from rest_framework import serializers
from .models import Restaurant, Menu

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address', 'latitude', 'longitude', 'owner', 'status']

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'name', 'description', 'price', 'image', 'restaurant']

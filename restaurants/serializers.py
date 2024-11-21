from rest_framework import serializers
from .models import Restaurant, Menu, Order

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address', 'latitude', 'longitude', 'owner', 'status']

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'name', 'description', 'price', 'image', 'restaurant']


class OrderSerializer(serializers.ModelSerializer):
    menu_items = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Menu.objects.all()
    )
    total_price = serializers.ReadOnlyField()
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Order
        fields = ['id', 'user', 'restaurant', 'menu_items', 'total_price', 'status', 'timestamp']

    def create(self, validated_data):
        menu_items = validated_data.pop('menu_items')  # Extract menu items from the validated data
        restaurant = validated_data['restaurant']  # Ensure the restaurant field is included
        total_price = sum(item.price for item in menu_items)  # Calculate total price
        order = Order.objects.create(
            **validated_data,
            total_price=total_price  # Set the calculated total price
        )
        order.menu_items.set(menu_items)  # Link the menu items to the order
        return order

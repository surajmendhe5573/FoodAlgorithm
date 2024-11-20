from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from .models import Restaurant, Menu
from .serializers import RestaurantSerializer, MenuSerializer
from rest_framework.permissions import IsAuthenticated

class RestaurantListView(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.query_params.get('status', None)
        latitude = self.request.query_params.get('latitude', None)
        longitude = self.request.query_params.get('longitude', None)

        if status:
            queryset = queryset.filter(status=status)

        if latitude and longitude:
            # Filter by geolocation (simple example, adjust as needed for distance calculation)
            queryset = queryset.filter(latitude=latitude, longitude=longitude)

        return queryset

class RestaurantCreateView(generics.CreateAPIView):
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Ensure the user is the restaurant owner
        serializer.save(owner=self.request.user)

    def check_permissions(self, request):
        if request.user.role != 'restaurant_owner':
            raise PermissionError("Only restaurant owners can create restaurants.")
        return super().check_permissions(request)

class RestaurantUpdateView(generics.UpdateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated]

    def check_permissions(self, request):
        # Ensure the user is the owner of the restaurant
        restaurant = self.get_object()
        if restaurant.owner != request.user:
            raise PermissionError("You are not the owner of this restaurant.")
        return super().check_permissions(request)

class MenuListView(generics.ListAPIView):
    serializer_class = MenuSerializer

    def get_queryset(self):
        restaurant_id = self.kwargs.get('restaurant_id')
        return Menu.objects.filter(restaurant_id=restaurant_id)

class MenuCreateView(generics.CreateAPIView):
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        restaurant = Restaurant.objects.get(id=self.kwargs['restaurant_id'])
        if restaurant.owner != self.request.user:
            raise PermissionError("You must be the restaurant owner to add a menu.")
        serializer.save(restaurant=restaurant)

    def check_permissions(self, request):
        restaurant = Restaurant.objects.get(id=self.kwargs['restaurant_id'])
        if restaurant.owner != request.user:
            raise PermissionError("You are not the owner of this restaurant.")
        return super().check_permissions(request)

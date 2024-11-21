from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import RestaurantListView, RestaurantCreateView, RestaurantUpdateView, MenuListView, MenuCreateView, OrderCreateView, OrderDetailView, OrderStatusUpdateView, UserOrderListView 


urlpatterns = [
    path('list/', RestaurantListView.as_view(), name='restaurant-list'),
    path('create/', RestaurantCreateView.as_view(), name='restaurant-create'),
    path('update/<int:pk>/', RestaurantUpdateView.as_view(), name='restaurant-update'),
    path('<int:restaurant_id>/menus/', MenuListView.as_view(), name='menu-list'),
    path('<int:restaurant_id>/menus/create/', MenuCreateView.as_view(), name='menu-create'),

    path('orders/', OrderCreateView.as_view(), name='order-create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('orders/<int:pk>/status/', OrderStatusUpdateView.as_view(), name='order-status-update'),
    path('orders/user/', UserOrderListView.as_view(), name='user-order-list'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

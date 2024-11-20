from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import RestaurantListView, RestaurantCreateView, RestaurantUpdateView, MenuListView, MenuCreateView

urlpatterns = [
    path('list/', RestaurantListView.as_view(), name='restaurant-list'),
    path('create/', RestaurantCreateView.as_view(), name='restaurant-create'),
    path('update/<int:pk>/', RestaurantUpdateView.as_view(), name='restaurant-update'),
    path('<int:restaurant_id>/menus/', MenuListView.as_view(), name='menu-list'),
    path('<int:restaurant_id>/menus/create/', MenuCreateView.as_view(), name='menu-create'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

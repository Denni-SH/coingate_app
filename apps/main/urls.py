from .views import index, create_order, get_orders_list
from django.urls import path


urlpatterns = [
    path('', index, name='index'),
    path('create_order', create_order, name='create_order'),
    path('order_list', get_orders_list, name='order_list'),
    
]

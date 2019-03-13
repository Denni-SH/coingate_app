from .views import IndexView, PaymentRedirectView, OrderListView
from django.urls import path


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create_order', PaymentRedirectView.as_view(), name='create_order'),
    path('order_list', OrderListView.as_view(), name='order_list'),
]

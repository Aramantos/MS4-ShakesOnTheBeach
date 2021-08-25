from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('collection', views.checkout_collection, name='checkout_collection'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    path('checkout_success_collection/<order_number>', views.checkout_success_collection, name='checkout_success_collection'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
]

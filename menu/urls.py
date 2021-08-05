from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('<product_id>', views.menu_product_detail, name='menu_product_detail'),
]

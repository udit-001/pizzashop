from django.urls import path
from .views import orders_cart, orders_list, orders_place

urlpatterns = [
    path('place/', orders_place, name="orders_place"),
    path('cart/', orders_cart, name="orders_cart"),
    path('', orders_list, name="orders_list"),

]

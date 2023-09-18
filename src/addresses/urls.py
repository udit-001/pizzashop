from django.urls import path
from .views import address_list, address_add, address_remove

urlpatterns = [
    path('', address_list, name="address_list"),
    path('add/', address_add, name="address_add"),
    path('remove/', address_remove, name="address_remove"),
]

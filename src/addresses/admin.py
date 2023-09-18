from django.contrib import admin
from .models import Address


class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'address_name', 'postal_code',
                    'address_line1', 'address_line2', 'city', 'state', 'landmark', 'is_deleted')
    list_display_links = ('customer', )
    list_filter = ('customer', 'state', 'is_deleted')
    search_fields = ('customer__username',
                     'customer__first_name', 'customer__email')


admin.site.register(Address, AddressAdmin)

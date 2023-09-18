from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import Order, OrderItem, Payment

# Register your models here.


class OrderItemInline(admin.StackedInline):
    model = Order.items.through
    extra = 1
    verbose_name = "Order Item"
    verbose_name_plural = "Order Items"
    # fields = Order.items.through._meta._get_fields()


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'quantity')
    list_display_links = ('name',)
    ordering = ('id',)
    search_fields = ('name',)
    list_per_page = 24


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'payment', 'started_date', 'ordered_date', 'status',
                    'is_ordered', 'get_order_total', 'get_items_count')
    list_display_links = ('customer',)
    inlines = [
        OrderItemInline
    ]
    list_filter = ('customer', 'is_ordered', 'started_date')
    exclude = ("items", )
    list_editable = ('status', 'is_ordered')
    ordering = ('started_date',)
    search_fields = ('started_date', 'customer__username',
                     'customer__first_name', 'customer__last_name', 'customer__email')

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id','stripe_charge_id', 'customer', 'amount')
    list_display_links = ('stripe_charge_id',)
    list_filter = ('customer', )


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Payment, PaymentAdmin)

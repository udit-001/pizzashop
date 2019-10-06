from decimal import Decimal

from django.contrib.auth.models import User
from django.db import models
from django.db.models import DecimalField, ExpressionWrapper, F, Sum

from addresses.models import Address

STATUS_CHOICES = (
    ("Pending", "Pending"),
    ("Confirmed", "Confirmed"),
    ("Preparing", "Preparing"),
    ("Cooking", "Cooking"),
    ("Arriving", "Arriving"),
    ("Delivered", "Delivered")
)


class OrderItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    items = models.ManyToManyField(OrderItem)
    started_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(blank=True, null=True)
    is_ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey(
        Address, on_delete=models.DO_NOTHING, null=True, blank=True)
    payment = models.ForeignKey(
        'Payment', on_delete=models.DO_NOTHING, null=True, blank=True)
    status = models.CharField(
        max_length=200, choices=STATUS_CHOICES, default="Pending")

    def get_order_total(self):
        total = Order.objects.get(id=self.id).items.aggregate(total_amount=ExpressionWrapper(
            Sum(F('price')*F('quantity')), output_field=DecimalField()))['total_amount']
        return round(Decimal(total), 2)
    get_order_total.short_description = "Total Amount"

    def get_items_count(self):
        return Order.objects.get(
            id=self.id).items.aggregate(Sum('quantity'))['quantity__sum']
    get_items_count.short_description = "Total Items"

    def __str__(self):
        return str(self.id)

class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=50)
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.stripe_charge_id)

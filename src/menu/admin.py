from django.contrib import admin

from .models import (Extra, Pasta, Platter, RegularPizza, Salad, SicilianPizza,
                     Sub, Topping)

# Register your models here.


class SaladAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    list_display_links = ('name',)
    ordering = ('id',)


class PlatterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'small_price', 'large_price')
    list_display_links = ('name',)
    search_fields = ('name',)
    list_per_page = 24
    ordering = ('id',)


class ToppingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name', 'id')
    search_fields = ('name', )
    ordering = ('id',)


class PastaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    list_display_links = ('name',)
    ordering = ('id',)


class PizzaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'small_price',
                    'large_price', 'no_of_toppings')
    list_display_links = ('name',)
    ordering = ('id',)


admin.site.register(Salad, SaladAdmin)
admin.site.register(Platter, PlatterAdmin)
admin.site.register(Topping, ToppingAdmin)
admin.site.register(Pasta, PastaAdmin)
admin.site.register(Sub, PlatterAdmin)
admin.site.register(Extra, ToppingAdmin)
admin.site.register(RegularPizza, PizzaAdmin)
admin.site.register(SicilianPizza, PizzaAdmin)

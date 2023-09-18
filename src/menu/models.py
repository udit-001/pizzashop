from django.db import models


class Salad(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Platter(models.Model):
    name = models.CharField(max_length=200)
    small_price = models.DecimalField(max_digits=10, decimal_places=2)
    large_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Pasta(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Extra(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Sub(models.Model):
    name = models.CharField(max_length=255)
    small_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    large_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class RegularPizza(models.Model):
    name = models.CharField(max_length=200)
    small_price = models.DecimalField(max_digits=10, decimal_places=2)
    large_price = models.DecimalField(max_digits=10, decimal_places=2)
    no_of_toppings = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name


class SicilianPizza(models.Model):
    name = models.CharField(max_length=200)
    small_price = models.DecimalField(max_digits=10, decimal_places=2)
    large_price = models.DecimalField(max_digits=10, decimal_places=2)
    no_of_toppings = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

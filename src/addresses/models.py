from django.contrib.auth.models import User
from django.db import models


class Address(models.Model):
    class Meta:
        verbose_name_plural = "addresses"
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    postal_code = models.CharField(max_length=120)
    address_name = models.CharField(max_length=120)
    address_line1 = models.CharField(max_length=120)
    address_line2 = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    landmark = models.CharField(max_length=120, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    def get_formatted_address(self):
        if self.landmark:
            return f"{self.address_line1}, {self.address_line2}, {self.city} {self.postal_code}, {self.state}, {self.landmark}"
        else:
            return f"{self.address_line1}, {self.address_line2}, {self.city} {self.postal_code}, {self.state}"

    def __str__(self):
        if self.landmark:
            return f"{self.address_line1}, {self.address_line2}, {self.city} {self.postal_code}, {self.state}, {self.landmark}"
        else:
            return f"{self.address_line1}, {self.address_line2}, {self.city} {self.postal_code}, {self.state}"

    get_formatted_address.short_description = "Formatted Address"

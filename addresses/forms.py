from django import forms
from .models import Address
from django.utils.translation import gettext_lazy as _
import requests

STATE_CHOICES = (
   ("AP","Andhra Pradesh"),
   ("AR","Arunachal Pradesh"),
   ("AS","Assam"),
   ("BR","Bihar"),
   ("CT","Chhattisgarh"),
   ("CH","Chandigarh"),
   ("DN","Dadra and Nagar Haveli"),
   ("DD","Daman and Diu"),
   ("DL","Delhi"),
   ("GA","Goa"),
   ("GJ","Gujarat"),
   ("HR","Haryana"),
   ("HP","Himachal Pradesh"),
   ("JK","Jammu and Kashmir"),
   ("JH","Jharkhand"),
   ("KA","Karnataka"),
   ("KL","Kerala"),
   ("MP","Madhya Pradesh"),
   ("MH","Maharashtra"),
   ("MN","Manipur"),
   ("ML","Meghalaya"),
   ("MZ","Mizoram"),
   ("NL","Nagaland"),
   ("OR","Orissa"),
   ("PB","Punjab"),
   ("PY","Pondicherry"),
   ("RJ","Rajasthan"),
   ("SK","Sikkim"),
   ("TN","Tamil Nadu"),
   ("TR","Tripura"),
   ("UP","Uttar Pradesh"),
   ("UK","Uttarakhand"),
   ("WB","West Bengal")
)

ADDRESS_CHOICES = (
    ('Home', 'Home Address'),
    ('Work', 'Work/Office Address'),
    ('Other', 'Other')
)


class AddressForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.customer = kwargs.pop('customer', None)
        super(AddressForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Address
        fields = ['postal_code', 'address_line1',
                  'address_line2', 'city', 'state', 'landmark', 'address_name']
        widgets = {
            'postal_code': forms.TextInput(attrs={'class': 'uk-input', 'type': 'number', 'placeholder': 'Enter Pincode', 'pattern': '^[1-9][0-9]{5}$'}),
            'address_line1': forms.TextInput(attrs={'class': 'uk-input', 'placeholder': 'Enter House No., Building Name'}),
            'address_line2': forms.TextInput(attrs={'class': 'uk-input', 'placeholder': 'Enter Road Name, Area, Colony'}),
            'city': forms.TextInput(attrs={'class': 'uk-input', 'placeholder': 'Enter City'}),
            'state': forms.Select(attrs={'class': 'uk-select'}, choices=STATE_CHOICES),
            'landmark': forms.TextInput(attrs={'class': 'uk-input', 'placeholder': 'Enter Landmark'}),
            'address_name': forms.RadioSelect(choices=ADDRESS_CHOICES)
        }
        labels = {
            'address_line1': _('House No., Building name'),
            'address_line2': _('Road Name, Area, Colony'),
            'postal_code': _('Pincode')
        }

    def clean_postal_code(self):
        postal_code = self.cleaned_data['postal_code']
        r = requests.get(f"https://api.postalpincode.in/pincode/{postal_code}")
        d = r.json()
        if d[0].get('Status') == 'Error':
            raise forms.ValidationError(
                _("This is an invalid pincode, try another one."))
        return postal_code
    
    def clean_address_name(self):
        address_name = self.cleaned_data['address_name']
        if Address.objects.filter(customer=self.customer, is_deleted=False, address_name=address_name).exists():
            raise forms.ValidationError(_(
                f"An address named {address_name} already exists. Try another name."
            ))
        return address_name
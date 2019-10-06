from allauth.account.adapter import DefaultAccountAdapter
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible
from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from validate_email import validate_email


class RestrictEmailAdapter(DefaultAccountAdapter):
    def clean_email(self, email):
        if not validate_email(email, check_mx=True, verify=True):
            raise forms.ValidationError(_("This is not a valid email. Try using another email."))
        return email



class SignupForm(forms.Form):
    captcha = ReCaptchaField(public_key=settings.RECAPTCHA_PUBLIC_KEY, private_key=settings.RECAPTCHA_PRIVATE_KEY, widget=ReCaptchaV2Invisible)
    first_name = forms.CharField(max_length=30, label='First Name', widget=forms.TextInput(attrs={
                                 'autocapitalize': 'words'}))
    last_name = forms.CharField(max_length=30, label='Last Name', widget=forms.TextInput(attrs={
        'autocapitalize': 'words'}))

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name'].title()
        user.last_name = self.cleaned_data['last_name'].title()
        user.save()

    def clean_first_name(self):
        data = self.cleaned_data['first_name']
        if not all(i.isalpha() or i.isspace() or i == "." for i in data):
            raise forms.ValidationError(
                _("This field cannot contain numbers or any special characters"))

        return data

    def clean_last_name(self):
        data = self.cleaned_data['last_name']
        if not all(i.isalpha() for i in data):
            raise forms.ValidationError(
                _("This field cannot contain numbers or any special characters"))

        return data

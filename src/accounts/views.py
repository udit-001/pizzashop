from pprint import pprint

from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.decorators.gzip import gzip_page

from orders.models import Order

# Create your views here.
def verify(request):
    return render(request, 'googlede0c6021e3b4b9c3.html', {})


@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request, 'accounts/profile.html', {})

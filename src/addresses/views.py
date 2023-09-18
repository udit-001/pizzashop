from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import HttpResponse, redirect, render
from django.views.decorators.http import require_POST

from orders.models import Order

from .forms import AddressForm
from .models import Address

# Create your views here.


@login_required
def address_add(request):
    if Order.objects.filter(
            customer=request.user, is_ordered=False).exists():
        request.session.__setitem__('cart', Order.objects.get(
            customer=request.user, is_ordered=False).get_items_count())
    else:
        request.session.__setitem__('cart', 0)
    order_next = request.GET.get('next', 0)
    if request.method == "POST":
        form = AddressForm(request.POST, customer=request.user)
        if form.is_valid():
            address = form.save(commit=False)
            address.customer = request.user
            address.save()
            if order_next:
                return redirect(order_next)
            else:
                messages.success(request, 'Address saved successfully!')
                return redirect('address_add')
        else:
            context = {
                'address_form': form
            }
            return render(request, 'addresses/address_add.html', context)
    else:

        context = {
            'address_form': AddressForm()
        }
        return render(request, 'addresses/address_add.html', context)

@login_required
def address_list(request):
    context = {
        'addresses': Address.objects.filter(customer=request.user, is_deleted=False)
    }
    return render(request, 'addresses/my_addresses.html', context)


@require_POST
def address_remove(request):
    address = Address.objects.get(id=request.POST.get('address'))
    address.is_deleted = True
    address.save()
    messages.success(request, 'Address removed successfully!')
    return redirect('address_list')

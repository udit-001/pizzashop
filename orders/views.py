from decimal import Decimal

import stripe
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum
from django.shortcuts import HttpResponse, redirect, render
from django.utils import timezone
from django.views.decorators.gzip import gzip_page

from addresses.models import Address
from menu.models import (Extra, Pasta, Platter, RegularPizza, Salad,
                         SicilianPizza, Sub, Topping)

from .models import Order, OrderItem, Payment


def address_check(user):
    return Address.objects.filter(customer=user, is_deleted=False).exists()


# Create your views here.
@login_required(login_url='/accounts/login/')
@user_passes_test(address_check, login_url='/address/add')
def orders_place(request):
    if request.method == "POST":
        try:
            if request.POST['form_name'] == 'reg_pizza':
                # Change name based on length of toppings
                toppings = ' - ' if request.POST.getlist(
                    'reg_toppings').__len__() > 0 else ' '
                name = f"{request.POST['size'].title()} Regular Pizza - {request.POST['pizza_name']} toppings{toppings}{', '.join(Topping.objects.filter(id__in=request.POST.getlist('reg_toppings')).values_list('name', flat=True))}"
                price = RegularPizza.objects.get(
                    no_of_toppings=request.POST['pizza_name']).__getattribute__(request.POST['size']+'_price')
                qty = request.POST['qty']

            elif request.POST['form_name'] == 'sic_pizza':
                # Change name based on length of toppings
                toppings = ' - ' if request.POST.getlist(
                    'sic_toppings').__len__() > 0 else ' '
                name = f"{request.POST['size'].title()} Sicilian Pizza - {request.POST['pizza_name']} toppings{toppings}{', '.join(Topping.objects.filter(id__in=request.POST.getlist('sic_toppings')).values_list('name', flat=True))}"
                price = SicilianPizza.objects.get(
                    no_of_toppings=request.POST['pizza_name']).__getattribute__(request.POST['size']+'_price')
                qty = request.POST['qty']

            elif request.POST['form_name'] == "sub":
                # Change name based on length of extras
                size, sub_id = request.POST['sub'].split('-')
                price = Sub.objects.get(
                    id=sub_id).__getattribute__(size+'_price') + Extra.objects.filter(id__in=request.POST.getlist('extra')).aggregate(Sum('price')).get('price__sum', Decimal(0.00))
                extra = ' with ' if request.POST.getlist(
                    'extra').__len__() > 0 else ' '
                name = f"{size.title()} Sub - {Sub.objects.get(id=sub_id).__getattribute__('name')}{extra}{', '.join(Extra.objects.filter(id__in=request.POST.getlist('extra')).values_list('name', flat=True))}"
                qty = request.POST['qty']

            elif request.POST['form_name'] == 'pasta':
                qty = request.POST['qty']
                name = f"Pasta - {Pasta.objects.get(id=request.POST['pasta']).__getattribute__('name')}"
                price = Pasta.objects.get(
                    id=request.POST['pasta']).__getattribute__('price')

            elif request.POST['form_name'] == 'salad':
                qty = request.POST['qty']
                name = f"Salad - {Salad.objects.get(id=request.POST['salad']).__getattribute__('name')}"
                price = Salad.objects.get(
                    id=request.POST['salad']).__getattribute__('price')

            elif request.POST['form_name'] == 'platter':
                size, platter_id = request.POST['platter'].split('-')
                price = Platter.objects.get(
                    id=platter_id).__getattribute__(size+'_price')
                name = f"{size.title()} Platter - {Platter.objects.get(id=platter_id).__getattribute__('name')}"
                qty = request.POST['qty']
        
        except KeyError as e:
            messages.error(request, 'Please fill all the required fields!')
            return redirect('orders_place')

        # Use get_or_create
        query = Order.objects.get_or_create(
            customer=request.user, is_ordered=False)
        order = query[0]

        if order.items.filter(name=name).exists():
            # Repeated Order
            # Increase quantity by 1
            p = order.items.get(name=name)

            p.quantity += int(qty)
            p.save()
            request.session.__setitem__(
                'cart', order.get_items_count())
        else:
            order_item = OrderItem.objects.create(
                name=name, price=price, quantity=qty)
            order.items.add(order_item)
            request.session.__setitem__(
                'cart', order.get_items_count())

        messages.success(request, 'Item added to cart!')
        return redirect('orders_place')

    context = {
        "toppings": Topping.objects.all().order_by('name'),
        "reg_pizza": RegularPizza.objects.all(),
        "sic_pizza": SicilianPizza.objects.all(),
        "pastas": Pasta.objects.all(),
        "salads": Salad.objects.all(),
        "platters": Platter.objects.all(),
        "subs": Sub.objects.all(),
        "extras": Extra.objects.all()
    }
    if Order.objects.filter(
            customer=request.user, is_ordered=False).exists():
        request.session.__setitem__('cart', Order.objects.get(
            customer=request.user, is_ordered=False).get_items_count())
    else:
        request.session.__setitem__('cart', 0)
    return render(request, 'orders/order.html', context)


@login_required(login_url='/accounts/login/')
def orders_cart(request):
    if request.method == "POST":
        if request.POST.get('stripeToken'):
            stripe.api_key = settings.STRIPE_KEY
            try:
                order = Order.objects.get(id=request.POST.get('order'))
                token = request.POST.get('stripeToken')
                amount = int(order.get_order_total()*100)
                charge = stripe.Charge.create(
                    amount=amount,
                    currency='usd',
                    description=f"Order #{order.id}",
                    source=token,
                    receipt_email=order.customer.email,
                )

                order.is_ordered = True

                payment = Payment()
                payment.stripe_charge_id = charge['id']
                payment.customer = request.user
                payment.amount = amount / 100
                payment.save()

                order.payment = payment
                order.shipping_address = Address.objects.get(id=request.POST.get('address'))
                order.ordered_date = timezone.now()
                order.save()

                request.session.__setitem__('cart', 0)

                messages.success(request, 'Your order is being processed. Payment successful!')
                return redirect('orders_cart')

            except stripe.error.CardError as e:
                messages.error(request, f"{err.get('message')}")
                return redirect('orders_cart')

            except stripe.error.RateLimitError as e:
                messages.error(request, "Rate limit error.")
                return redirect('orders_cart')

            except stripe.error.InvalidRequestError as e:
                print(e)
                messages.error(request, "Invalid parameters.")
                return redirect('orders_cart')

            except stripe.error.AuthenticationError as e:
                messages.error(request, "Not Authenticated")
                return redirect('orders_cart')

            except stripe.error.APIConnectionError as e:
                messages.error(request, "Network error")
                return redirect('orders_cart')

            except stripe.error.StripeError as e:
                messages.error(request, "Something went wrong. You were not charged please try again.")
                return redirect('orders_cart')

            except Exception as e:
                # Send an email to ourselves
                messages.error(request, "Serious error occurred. We have been notified.")
                return redirect('orders_cart')

        elif request.POST.get('remove'):
            Order.objects.get(id=request.POST['order_id']).items.remove(
                OrderItem.objects.get(id=request.POST.get('remove')))
            OrderItem.objects.get(id=request.POST.get('remove')).delete()
            request.session.__setitem__('cart', Order.objects.get(
                id=request.POST['order_id']).get_items_count())
            if Order.objects.get(id=request.POST['order_id']).items.count() == 0:
                Order.objects.get(id=request.POST['order_id']).delete()
                request.session.__setitem__('cart', 0)

            messages.success(request, 'Item removed successfully!')
            return redirect('orders_cart')

    context = {
        "cart": Order.objects.filter(customer=request.user, is_ordered=False).first(),
        "addresses": Address.objects.filter(customer=request.user, is_deleted=False),
    }
    return render(request, 'orders/cart.html', context)


@login_required(login_url='/accounts/login/')
def orders_list(request):
    context = {
        "orders": Order.objects.select_related('payment', 'shipping_address').prefetch_related('items').filter(customer=request.user, is_ordered=True).order_by('-ordered_date')
    }
    return render(request, 'orders/my_orders.html', context)

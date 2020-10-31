from django.shortcuts import render, redirect
from django.contrib.sessions.backends.db import SessionStore
from django.conf import settings
from django.views.generic import DetailView, ListView
from django.http import HttpResponse, HttpRequest, JsonResponse

import traceback

from accounts.forms import LoginForm, GuestForm
from accounts.models import GuestEmail
from addresses.forms import AddressForm
from addresses.models import Address
from billing.models import BillingProfile
from orders.models import Order
from products.models import Product
from .models import Cart, CartItem

STRIPE_PUB_KEY = getattr(settings,"STRIPE_PUB_KEY",None)

class CartHome(ListView):
    template_name = "carts/home.html"

    def get(self, request):
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        print(cart_obj.is_digital)
        context = {
            "cart_obj": cart_obj,
        }
        return render(request,"carts/home.html", context)

def cart_update(request, *args, **kwargs):
    item_added = False
    item_removed = False
    item_updated = False
    cart_item_id = request.POST.get('cart_item_id', None)
    cart_item_update = request.POST.get('cart_item_update', False)
    cart_item_remove = request.POST.get('cart_item_remove', False)
    cart_item_add = request.POST.get('cart_item_add', False)

    if cart_item_add is False:
        cart_item_add = request.POST.get('cartItemAdd', False)

    if cart_item_update is False:
        cart_item_update = request.POST.get('cartItemUpdate', False)

    if cart_item_remove is False:
        cart_item_remove = request.POST.get('cartItemRemove', False)

    product_id = request.POST.get("product_id", None)
    product_quantity = request.POST.get('product_quantity', None)
    try:
        product_obj = Product.objects.get(id=product_id)
    except:
        product_obj = False


    if product_obj:
        cart_obj, new_obj = Cart.objects.new_or_get(request)

        if cart_item_remove:
            cart_item_obj = CartItem.objects.get(id=cart_item_id)
            cart_obj.cart_items.remove(cart_item_obj)
            total, vat_total, sub_total = Cart.objects.calculate_cart_total(request, cart_obj=cart_obj)
            if total and vat_total and sub_total:
                cart_obj.total = total
                cart_obj.vat_total = vat_total
                cart_obj.subtotal = sub_total
                cart_obj.save()
            item_removed = True
            request.session['cart_item_count'] = cart_obj.cart_items.count()

        if cart_item_update:
            cart_item_obj = CartItem.objects.get(id=cart_item_id)

            if int(product_quantity) != int(cart_item_obj.quantity):
                cart_item_obj.quantity = product_quantity
                cart_item_obj.save()
                total, vat_total, sub_total = Cart.objects.calculate_cart_total(request, cart_obj=cart_obj)
                if total and vat_total and sub_total:
                    cart_obj.total = total
                    cart_obj.vat_total = vat_total
                    cart_obj.subtotal = sub_total
                    cart_obj.save()
            item_updated = True


        if cart_item_add:
            cart_item_obj, new_item_obj = CartItem.objects.new_or_get(request, product_obj=product_obj)
            cart_item_obj.quantity = product_quantity
            cart_item_obj.save()
            cart_obj.cart_items.add(cart_item_obj)
            cart_item_id = cart_item_obj.id
            total, vat_total, sub_total = Cart.objects.calculate_cart_total(request, cart_obj=cart_obj)
            if total and vat_total and sub_total:
                cart_obj.total = total
                cart_obj.vat_total = vat_total
                cart_obj.subtotal = sub_total
                cart_obj.save()
            item_added = True
        request.session['cart_item_count'] = cart_obj.cart_items.count()


        if request.is_ajax():
            json_data= {
                "added": item_added,
                "removed": item_removed,
                "updated": item_updated,
            }
            if cart_item_id:
                json_data.update({
                    "cart_item_id": cart_item_id
                })
            return JsonResponse(json_data)
    return redirect("cart:home")

def checkout_home(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    order_obj = None
    if cart_created or cart_obj.cart_items.count() == 0:
        redirect("cart:home")

    login_form = LoginForm(request=request)
    guest_form = GuestForm(request=request)
    address_form = AddressForm
    billing_address_id = request.session.get("billing_address_id", None)

    shipping_address_required = not cart_obj.is_digital

    shipping_address_id = request.session.get("shipping_address_id", None)
    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
    address_qs = None
    has_card = False
    if billing_profile is not None:
        if request.user.is_authenticated:
            address_qs = Address.objects.filter(billing_profile=billing_profile)
        order_obj = Order.objects.new_or_get(billing_profile, cart_obj)
        if shipping_address_id:
            order_obj.shipping_address = Address.objects.get(id=shipping_address_id)
            del request.session["shipping_address_id"]
        if billing_address_id:
            order_obj.billing_address = Address.objects.get(id=billing_address_id)
            del request.session["billing_address_id"]
        if billing_address_id or shipping_address_id:
            order_obj.save()
        has_card = billing_profile.has_card
    if request.method == "POST":
        is_prepared = order_obj.check_done()
        print(is_prepared)
        if is_prepared:
            did_charge, crg_msg = billing_profile.charge(order_obj)
            if did_charge:
                order_obj.mark_paid()
                request.session['cart_item_count'] = 0
                del request.session['cart_id']
                if not billing_profile.user:
                    billing_profile.set_cards_inactive() # is this the right spot for this?
                return redirect("cart:success")
            else:
                return redirect("cart:checkout")
    context = {
        "object": order_obj,
        "billing_profile": billing_profile,
        "login_form": login_form,
        "guest_form": guest_form,
        "address_form": address_form,
        "address_qs": address_qs,
        "has_card": has_card,
        "publish_key": STRIPE_PUB_KEY,
        "shipping_address_required": shipping_address_required
    }
    return render(request, "carts/checkout.html",context)

def checkout_done_view(request):
    return render(request, "carts/checkout-done.html", {})
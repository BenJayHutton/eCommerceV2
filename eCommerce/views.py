from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

import os
from carts.models import Cart, CartItem
from products.models import Product, ItemTag
from .forms import ContactForm

class DefaultHomePage(TemplateView):
    display_name="home"
    featured = Product.objects.all().featured()
    tag_item_books_obj = ItemTag.objects.all().get_product_by_tag_name("Books")

    def get(self, request):
        context = {}
        visitor_name = request.session.get("first_name")
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        context['cart_obj'] = cart_obj
        cart_item_id = {}
        context['cart_item_id'] = cart_item_id
        cart_item_obj = []
        for items in cart_obj.cart_items.all():
            cart_item_obj.append(items.product)
            cart_item_id[items.product] = int(items.id)

        if self.display_name == "home":
            context = {
                "title": "Home Page",
                "content": "Welcome to the home page",
                "featured": self.featured,
                "tag_item_books_obj": self.tag_item_books_obj,
                'cart_item_obj': cart_item_obj
                }
        elif self.display_name == "about":
            context = {
                "title": "About Page",
                "content": "Welcome to the about page"
                }
        if request.user.is_authenticated:
            context["premium_content"] = "Premium"

        if visitor_name is not None:
            context["first_name"] = visitor_name
        else:
            context["first_name"] = "New visitor"
        return render(request, "home_page.html", context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact Page",
        "form": contact_form,
        }
    if contact_form.is_valid():
        if request.is_ajax():
            return JsonResponse({"message": "Thank you for your submission"})
    return render(request, "contact/view.html", context)


def about_page(request):
    context = {
        "title": "About Page",
        }
    return render(request, "about.html", context)

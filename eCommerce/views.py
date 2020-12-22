from django.http import HttpResponse, JsonResponse, HttpRequest
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView

from carts.models import Cart, CartItem
from products.models import Product, Tag
from .forms import ContactForm


class DefaultHomePage(TemplateView):
    display_name="home"
    model = Product
    tags_obj = Tag

    products_books_obj = model.objects.filter(tags__name="Books", tags__public=True)
    products_fantasy_obj = model.objects.filter(tags__name="Fantasy", tags__public=True)
    products_apparel_obj = model.objects.filter(tags__name="Apparel", tags__public=True)
    products_digital_obj = model.objects.filter(tags__name="Digital", tags__public=True)

    def get(self, request):
        context = {}
        visitor_name = request.session.get("first_name")
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        context['cart_obj'] = cart_obj
        cart_item_id = {}
        context['cart_item_id'] = cart_item_id
        cart_item_obj = []
        # print("products_digital_obj ", self.products_digital_obj.count())
        for items in cart_obj.cart_items.all():
            cart_item_obj.append(items.product)
            cart_item_id[items.product] = int(items.id)
        if self.display_name == "home":
            context = {
                "title": "Home Page",
                "content": "Welcome to the home page",
                "description": "Buy high-quality products ranging from books to apparel",
                "products_books_obj": self.products_books_obj,
                "products_apparel_obj": self.products_apparel_obj,
                "products_digital_obj": self.products_digital_obj,
                'cart_item_obj': cart_item_obj,
                'cart_item_id': cart_item_id,
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
        #print(context)
        return render(request, "home_page.html", context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "description": "Contat Page",
        "title": "Contact Page",
        "form": contact_form,
        }
    if contact_form.is_valid():
        if request.is_ajax():
            return JsonResponse({"message": "Thank you for your submission"})
    return render(request, "contact/view.html", context)


def about_page(request):
    context = {
        "description": "About page",
        "title": "About Page",
        }
    return render(request, "about.html", context)

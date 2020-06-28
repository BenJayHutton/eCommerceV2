from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from products.models import Product


class DefaultHomePage(TemplateView):
    display_name="home"
    featured = Product.objects.all().featured()

    def get(self, request):
        print(self.featured)
        if self.display_name == "home":
            context = {
                "title": "Home Page",
                "content": "Welcome to the home page",
                "featured": self.featured
                }
        elif self.display_name == "about":
            context = {
                "title": "About Page",
                "content": "Welcome to the about page"
                }
        if request.user.is_authenticated:
            context["premium_content"] = "Premium"
        return render(request, "home_page.html", context)
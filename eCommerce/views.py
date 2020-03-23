from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from products.models import *


def home_page(request):
    # print(request.session.get("first_name", "Unknown"))
    #featured = Product.objects.all().featured()
    context = {
        "title": "Home Page",
        "content": "Welcome to the home page",
        #"featured": featured
        }
    if request.user.is_authenticated:
        context["premium_content"] = "Premium"
    return render(request, "home_page.html", context)


def about_page(request):
    context = {
        "title": "About Page",
        "content": "Welcome to the about page"
        }
    return render(request, "home_page.html", context)

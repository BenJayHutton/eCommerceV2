from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from products.models import *


class DefaultHomePage(TemplateView):
    display_name="home"

    def get(self, request):
        if self.display_name == "home":
            context = {
                "title": "Home Page",
                "content": "Welcome to the home page",
                }
        elif self.display_name == "about":
            context = {
                "title": "About Page",
                "content": "Welcome to the about page"
                }
        if request.user.is_authenticated:
            context["premium_content"] = "Premium"
        return render(request, "home_page.html", context)
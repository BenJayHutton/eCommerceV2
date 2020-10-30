from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

import os
from products.models import Product
from .forms import ContactForm


class DefaultHomePage(TemplateView):
    display_name="home"
    featured = Product.objects.all().featured()
    

    def get(self, request):
        visitor_name = request.session.get("first_name")
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

        if visitor_name is not None:
            context["first_name"] = visitor_name
        else:
            context["first_name"] = "New visitor"
        return render(request, "home_page.html", context)

        
def contact_page(request):
    # send_mail(
    #     'Test Subject',
    #     'Test',
    #     os.environ.get("DEFAULT_FROM_EMAIL", None),
    #     [os.environ.get("DEFAULT_FROM_EMAIL", None)],
    #     fail_silently=False,
    # )
    return HttpResponse("contact")
    # contact_form = ContactForm(request.POST or None)
    # context = {
    #     "title": "Contact Page",
    #     "content": "Welcome to the contact page",
    #     "form": contact_form,
    #     }
    # if contact_form.is_valid():
    #     if request.is_ajax():
    #         return JsonResponse({"message": "Thank you for your submission"})
    # return render(request, "contact/view.html", context)


def about_page(request):
    context = {
        "title": "About Page",
        }
    return render(request, "about.html", context)
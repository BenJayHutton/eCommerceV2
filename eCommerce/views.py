from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from products.models import Product
from .forms import ContactForm, LoginForm, RegisterForm


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
    


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
    "title": "Login Page",
    "content": "Login page",
    "form": form,
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect("/")        
        else:
            # Return an 'invalid login' error message.
            print("wrong details")
    return render(request, "auth/login.html", context)

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "title": "Register Page",
        "content": "Register page",
        "form": form,
    }
   
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        print(form.cleaned_data)
        new_user = User.objects.create_user(username, email, password)
        print("user created: ", new_user)

    return render(request, "auth/register.html", context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact Page",
        "content": "Welcome to the contact page",
        "form": contact_form,
        }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
        if request.is_ajax():
            return JsonResponse({"message": "Thank you for your submission"})
    return render(request, "contact/view.html", context)
from django import forms
from django.contrib.auth import get_user_model

# User = get_user_model()


class ContactForm(forms.Form):
    fullname    = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "id": "form_full_name", "placeholder": "Your full name"}))
    email       = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "email"}))
    content     = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "content..."}))

from django.shortcuts import render
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DetailView,
    TemplateView,
)

from .models import EbayAccount


class EbaySearchListing(TemplateView):
    def get(self, request):
        context = {}
        return render(request, "ebay/index.html", context)

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
        ebay_account = EbayAccount.objects.all().filter(user=request.user).first()
        print(ebay_account)
        context = {
            'ebay_account':ebay_account,
        }
        return render(request, "ebay/index.html", context)

from django.shortcuts import render
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DetailView,
    TemplateView,
)

from .utils import EbaySearch
from .models import EbayAccount


class EbaySearchListing(TemplateView):

    def get(self, request):
        ebay_account = EbayAccount.objects.all().filter(user=request.user).first()
        api_key = None
        result = None
        search = "Harry potter"
        if ebay_account:
            api_key = ebay_account.production_api_key

        # if api_key is not None:
        #     result = EbaySearch.find_items_by_product(api_key=api_key, search=search)

        context = {
            'result': result,
        }
        return render(request, "ebay/index.html", context)

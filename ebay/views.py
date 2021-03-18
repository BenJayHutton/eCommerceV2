from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DetailView,
    TemplateView,
)

import urllib.parse
import requests
from .forms import EbaySearchForm
from .models import EbayAccount


class EbayMerchendiseApi(TemplateView):

    def getMostWatchedItems(self):
        return "getMostWatchedItems"


class EbayShoppingApi(TemplateView):
    template_name = 'ebay_finding_api.html'
    base_url = "https://open.api.ebay.com/shopping?"

    def find_products(self, *args, **kwargs):
        api_key = kwargs.get("api_key", None)
        search = urllib.parse.quote(kwargs.get("search", None))
        url = self.base_url+"callname=FindProducts&responseencoding=JSON&appid=" + api_key + "&siteid=0&version=967&QueryKeywords=" + search + "&AvailableItemsOnly=true&MaxEntries=2"
        response = requests.get(url)

        return response.json()


class EbaySearchListing(TemplateView):
    form_class = EbaySearchForm
    EbayShoppingApi = EbayShoppingApi()
    EbayMerchendiseApi = EbayMerchendiseApi()

    def get(self, request):

        context = {
            'form': self.form_class,
            'EbayMerchendiseApi': self.EbayMerchendiseApi,
        }
        return render(request, "ebay/index.html", context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        user = request.user
        ebay_production_key = EbayAccount.objects.all().filter(user=user).first().production_api_key
        if form.is_valid():
            result = self.EbayShoppingApi.find_products(search=form.cleaned_data['search'], api_key=ebay_production_key)

        context = {
            'result': result,
            'form': self.form_class,
        }
        return render(request, "ebay/index.html", context)

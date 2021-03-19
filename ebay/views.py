from django.contrib.auth import get_user_model
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

import requests
import urllib
from .forms import EbaySearchForm
from .models import EbayAccount


class EbayMerchendiseApi(TemplateView):

    def getMostWatchedItems(self):
        return "getMostWatchedItems"


class EbayShoppingApi(TemplateView):
    template_name = "ebay_finding_api.html"
    responseencoding = "JSON"
    base_url = "https://open.api.ebay.com/shopping?" \
               "callname={callname}&" \
               "responseencoding={responseencoding}&" \
               "appid={api_key}&" \
               "siteid=0&" \
               "version=967&" \
               "QueryKeywords={search}&" \
               "AvailableItemsOnly=true&" \
               "MaxEntries=2"

    def find_products(self, *args, **kwargs):
        api_key = kwargs.get("api_key", None)
        search = urllib.parse.quote(kwargs.get("search", None))
        call_name = "FindProducts"
        url = self.base_url.format(
            base_url=self.base_url,
            callname=call_name,
            api_key=api_key,
            responseencoding=self.responseencoding,
            search=search)

        response = requests.get(url)
        return response.json()

    def get_category_info(self, **kwargs):
        api_key = kwargs.get("api_key", None)
        url_search = urllib.parse.quote(kwargs.get("search", " "))
        call_name = "GetCategoryInfo"
        return self.base_url.format(
                    base_url=self.base_url,
                    callname=call_name,
                    api_key=api_key,
                    responseencoding=self.responseencoding,
                    search=url_search)

    def get_ebay_time(self):
        api_key = kwargs.get("api_key", None)
        url_search = urllib.parse.quote(kwargs.get("search", " "))
        call_name = "GeteBayTime"
        return self.base_url.format(
            base_url=self.base_url,
            callname=call_name,
            api_key=api_key,
            responseencoding=self.responseencoding,
            search=url_search)

    def get_item_status(self):
        api_key = kwargs.get("api_key", None)
        url_search = urllib.parse.quote(kwargs.get("search", " "))
        call_name = "GetItemStatus"
        return self.base_url.format(
            base_url=self.base_url,
            callname=call_name,
            api_key=api_key,
            responseencoding=self.responseencoding,
            search=url_search)

    def get_multiple_items(self):
        api_key = kwargs.get("api_key", None)
        url_search = urllib.parse.quote(kwargs.get("search", " "))
        call_name = "GetMultipleItems"
        return self.base_url.format(
            base_url=self.base_url,
            callname=call_name,
            api_key=api_key,
            responseencoding=self.responseencoding,
            search=url_search)

    def get_shipping_costs(self):
        api_key = kwargs.get("api_key", None)
        url_search = urllib.parse.quote(kwargs.get("search", " "))
        call_name = "GetShippingCosts"
        return self.base_url.format(
            base_url=self.base_url,
            callname=call_name,
            api_key=api_key,
            responseencoding=self.responseencoding,
            search=url_search)

    def get_single_item(self):
        api_key = kwargs.get("api_key", None)
        url_search = urllib.parse.quote(kwargs.get("search", " "))
        call_name = "GetSingleItem"
        return self.base_url.format(
            base_url=self.base_url,
            callname=call_name,
            api_key=api_key,
            responseencoding=self.responseencoding,
            search=url_search)

    def get_user_profile(self):
        api_key = kwargs.get("api_key", None)
        url_search = urllib.parse.quote(kwargs.get("search", " "))
        call_name = "GetUserProfile"
        return self.base_url.format(
            base_url=self.base_url,
            callname=call_name,
            api_key=api_key,
            responseencoding=self.responseencoding,
            search=url_search)


class EbaySearchListing(TemplateView):
    form_class = EbaySearchForm
    EbayShoppingApi = EbayShoppingApi()
    EbayMerchendiseApi = EbayMerchendiseApi()

    def get(self, request):

        context = {
            'form': self.form_class,
            'EbayMerchendiseApi': self.EbayMerchendiseApi,
            'EbayShoppingApi': self.EbayShoppingApi,
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

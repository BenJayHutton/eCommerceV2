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
import json
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
               "version=967"
    headers = {}

    def find_products(self, **kwargs):
        api_key = kwargs.get("api_key", None)
        search = urllib.parse.quote(kwargs.get("search", None))
        call_name = "FindProducts"
        url = self.base_url+"&QueryKeywords={search}&" \
               "AvailableItemsOnly=true&" \
               "MaxEntries=2"
        response = requests.get(url.format(
            base_url=self.base_url,
            callname=call_name,
            api_key=api_key,
            responseencoding=self.responseencoding,
            search=search))
        return response.json()

    def get_category_info(self, **kwargs):
        api_key = kwargs.get("api_key", None)
        item_id = urllib.parse.quote(kwargs.get("itemId", " "))
        call_name = "GetCategoryInfo"
        return self.base_url.format(
                    base_url=self.base_url,
                    callname=call_name,
                    api_key=api_key,
                    responseencoding=self.responseencoding,
                    search=url_search)

    def get_ebay_time(self, **kwargs):
        api_key = kwargs.get("api_key", None)
        url_search = urllib.parse.quote(kwargs.get("search", " "))
        call_name = "GeteBayTime"
        return self.base_url.format(
            base_url=self.base_url,
            callname=call_name,
            api_key=api_key,
            responseencoding=self.responseencoding,
            search=url_search)

    def get_item_status(self, **kwargs):
        api_key = kwargs.get("api_key", None)
        item_id = urllib.parse.quote(kwargs.get("ItemId", " "))
        url = self.base_url + "&ItemId={item_id}"
        call_name = "GetItemStatus"
        return url.format(
            base_url=self.base_url,
            callname=call_name,
            api_key=api_key,
            responseencoding=self.responseencoding,
            item_id=item_id)

    def get_multiple_items(self, **kwargs):
        api_key = kwargs.get("api_key", None)
        url = self.base_url + "&ItemId={item_id}"
        item_id = urllib.parse.quote(kwargs.get("ItemId", " "))
        call_name = "GetMultipleItems"
        return url.format(
            base_url=self.base_url,
            callname=call_name,
            api_key=api_key,
            responseencoding=self.responseencoding,
            item_id=item_id)

    def get_shipping_costs(self, **kwargs):
        api_key = kwargs.get("api_key", None)
        url_search = urllib.parse.quote(kwargs.get("search", " "))
        call_name = "GetShippingCosts"
        return self.base_url.format(
            base_url=self.base_url,
            callname=call_name,
            api_key=api_key,
            responseencoding=self.responseencoding,
            search=url_search)

    def get_single_item(self, **kwargs):
        api_key = kwargs.get("api_key", None)
        url_search = urllib.parse.quote(kwargs.get("search", " "))
        call_name = "GetSingleItem"
        return self.base_url.format(
            base_url=self.base_url,
            callname=call_name,
            api_key=api_key,
            responseencoding=self.responseencoding,
            search=url_search)

    def get_user_profile(self, **kwargs):
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
        user = request.user
        ebay_production_key = EbayAccount.objects.all().filter(user=user).first().production_api_key
        get_multiple_items = self.EbayShoppingApi.get_multiple_items(api_key=ebay_production_key)

        context = {
            'form': self.form_class,
            'EbayMerchendiseApi': self.EbayMerchendiseApi,
            'get_multiple_items': get_multiple_items,
        }
        return render(request, "ebay/index.html", context)

    def post(self, request, *args, **kwargs):
        response = HttpResponse()
        form = self.form_class(request.POST)
        user = request.user
        ebay_production_key = EbayAccount.objects.all().filter(user=user).first().production_api_key

        if form.is_valid():
            print(response)
            form_select_api = form.cleaned_data['api_choice']
            form_search_api = form.cleaned_data['search']
            if form_select_api == "FindProducts":
                result = self.EbayShoppingApi.find_products(search=form_search_api, api_key=ebay_production_key)
            elif form_select_api == "GetCategoryInfo":
                result = self.EbayShoppingApi.get_category_info(search=form_search_api, api_key=ebay_production_key)
            elif form_select_api == "GeteBayTime":
                result = self.EbayShoppingApi.get_ebay_time(search=form_search_api, api_key=ebay_production_key)
            elif form_select_api == "GetItemStatus":
                result = self.EbayShoppingApi.get_item_status(search=form_search_api, api_key=ebay_production_key)
            elif form_select_api == "GetMultipleItems":
                result = self.EbayShoppingApi.get_multiple_items(search=form_search_api, api_key=ebay_production_key)
            elif form_select_api == "GetShippingCosts":
                result = self.EbayShoppingApi.get_shipping_costs(search=form_search_api, api_key=ebay_production_key)
            elif form_select_api == "GetSingleItem":
                result = self.EbayShoppingApi.get_single_item(search=form_search_api, api_key=ebay_production_key)
            elif form_select_api == "GetUserProfile":
                result = self.EbayShoppingApi.get_user_profile(search=form_search_api, api_key=ebay_production_key)
            else:
                result = None

        context = {
            'result': result,
            'form': self.form_class,
        }
        return render(request, "ebay/index.html", context)

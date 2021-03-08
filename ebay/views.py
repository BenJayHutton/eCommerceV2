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

from .utils import EbaySearch, EbayFindingApi
from .forms import EbaySearchForm
from .models import EbayAccount


class EbaySearchListing(TemplateView):
    form_class = EbaySearchForm

    def get(self, request):

        context = {
            'form': self.form_class,
        }
        return render(request, "ebay/index.html", context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        user = request.user
        ebay_production_key = EbayAccount.objects.all().filter(user=user).first().production_api_key
        if form.is_valid():
            result = EbaySearch.find_items_by_product(self, search=form.cleaned_data['search'], api_key=ebay_production_key)
        if result['Ack'] == "Success":
            for product in result['Product']:
                for ProductID in product['ProductID']:
                    if ProductID['Type'] =='Reference':
                        print(EbayFindingApi.find_items_by_product(self, api_key=ebay_production_key, product_id=ProductID['Value']))
                        # print(ProductID['Value'])
        context = {
            'result': result,
            'form': self.form_class,
        }
        return render(request, "ebay/index.html", context)


class EbayFindingApi(TemplateView):
    #template_name = 'ebay_finding_api.html'

    def get(self, request, *args, **kwargs):
        search = kwargs.get('search')
        context = {
            "search": search,
        }
        print("search", search)
        print("args", args)
        print("kwargs", kwargs)
        return render(request, "ebay/ebay_finding_api.html", context)
        # api_key = None
        # result = None
        # request = self.request
        # search_ = "Harry Potter"
        # json_response = kwargs.get("json_response", None)
        # json_return = []
        # for product in json_response['Product']:
        #     for productID in product['ProductID']:
        #         json_return.append(productID)
        # ebay_account = EbayAccount.objects.all().filter(user=request.user).first()
        # if ebay_account:
        #     api_key = ebay_account.production_api_key
        #
        # if api_key is not None:
        #     result = EbaySearch.find_items_by_product(self, api_key=api_key, search=search_)
        #
        # context = {
        #     'result': result,
        # }
        #return render(request, "ebay/index.html", context)

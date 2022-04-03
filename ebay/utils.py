from django.views.generic import TemplateView
import urllib.parse
import requests


class EbaySearch(TemplateView):
    base_url = "https://open.api.ebay.com"

    def ebay_basic_search(self, search, api_key):
        # api_key = api_key
        # return_text = search
        # return return_text+" - "+api_key
        return self.base_url

    def find_items_by_product(self, **kwargs):
        api_key = kwargs.get("api_key", None)
        search = urllib.parse.quote(kwargs.get("search", None))
        url = "https://open.api.ebay.com/shopping?callname=FindProducts&responseencoding=JSON&appid="+api_key+"&siteid=0&version=967&QueryKeywords="+search+"&AvailableItemsOnly=true&MaxEntries=2"
        response = requests.get(url)
        json_response = response.json()
        return json_response

    def get_single_item(self, **kwargs):
        api_key = kwargs.get("api_key", None)
        item_id = kwargs.get("item_id", None)
        url = "https://open.api.ebay.com/shopping?callname=GetSingleItem&responseencoding=JSON&appid="+api_key+"&siteid=0&version=967&ItemID="+item_id+"&IncludeSelector=Variations,ItemSpecifics"
        return url


class EbayFindingApi(TemplateView):
    base_url_ = "test.com"

    def find_items_by_product(self, **kwargs):
        api_key = kwargs.get("api_key", None)
        product_id = kwargs.get("product_id", None)
        url = "https://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsByProduct&SERVICE-VERSION=1.0.0&SECURITY-APPNAME="+api_key+"&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD&paginationInput.entriesPerPage=2&productId.@type=ReferenceID&productId="+product_id
        return url

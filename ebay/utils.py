from django.views import View
import urllib.parse
import requests


class EbaySearch(View):
    base_url = "https://open.api.ebay.com"

    def ebay_basic_search(self, search, api_key):
        api_key = api_key
        return_text = search
        return return_text+" - "+api_key

    def find_items_by_product(self, **kwargs):
        api_key = kwargs.get("api_key", None)
        search = urllib.parse.quote(kwargs.get("search", None))
        url = "https://open.api.ebay.com/shopping?callname=FindProducts&responseencoding=JSON&appid="+api_key+"&siteid=0&version=967&QueryKeywords="+search+"&AvailableItemsOnly=true&MaxEntries=2"
        response = requests.get(url)
        json_response = response.json()
        return json_response

    def find_single_item(self, **kwargs):
        pass
        # https://open.api.ebay.com/shopping?callname=GetSingleItem&responseencoding=JSON&
        # appid=YourAppIDHere&
        # siteid=0&
        # version=967 &

        # IncludeSelector = Variations, ItemSpecifics

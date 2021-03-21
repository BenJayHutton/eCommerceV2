from django import forms

SEARCH_SHOPPING_API_CHOICES = [
    ('FindProducts', 'Find Products'),
    ('GetCategoryInfo', 'Get Category Info'),
    ('GeteBayTime', 'Get eBay Time'),
    ('GetItemStatus', 'Get Item Status'),
    ('GetMultipleItems', 'Get Multiple Items'),
    ('GetShippingCosts', 'Get Shipping Costs'),
    ('GetSingleItem', 'Get Single Item'),
    ('GetUserProfile', 'Get User Profile'),
]

class EbaySearchForm(forms.Form):
    search = forms.CharField(label='', widget=forms.TextInput(attrs={"class": "form-control", "id": "ebay_search", "placeholder": "Search Ebay"}))
    api_choice = forms.ChoiceField(widget=forms.RadioSelect, choices=SEARCH_SHOPPING_API_CHOICES)

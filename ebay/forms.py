from django import forms


class EbaySearchForm(forms.Form):
    search = forms.CharField(label='', widget=forms.TextInput(attrs={"class": "form-control", "id": "ebay_search", "placeholder": "Search Ebay"}))

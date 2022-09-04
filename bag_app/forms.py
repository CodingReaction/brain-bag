from django import forms
from .models import Bag, Term


class AutofillBagForm(forms.Form):
    url = forms.CharField(label="Url to scrappe", max_length=300)
    parent_selector = forms.CharField(label="CSS Parent selector", max_length=100)
    children_selector = forms.CharField(label="CSS Children selector", max_length=100, empty_value= "a")
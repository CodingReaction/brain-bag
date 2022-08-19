from django import forms
from .models import Bag

class BagForm(forms.Form):
    bag_name = forms.CharField(label="Name of the new BAG", max_length=100)


class TermForm(forms.Form):
    term_name = forms.CharField(label="Name of the new TERM", max_length=50)
    term_url = forms.URLField(label="Link with info", max_length=200)
    term_bag = forms.ModelChoiceField(queryset=Bag.objects.all(), empty_label=None)
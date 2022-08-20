from django import forms
from .models import Bag, Term

class BagForm(forms.Form):
    bag_name = forms.CharField(label="Name of the new BAG", max_length=100)


class TermForm(forms.ModelForm):
    class Meta:
        model = Term
        fields = ("name", "url", "bag")
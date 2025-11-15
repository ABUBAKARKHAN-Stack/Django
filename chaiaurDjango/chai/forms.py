from django import forms
from .models import ChaiVariety


class ChaiVarietyForm(forms.Form):
    chai_variety = forms.ModelChoiceField(
        queryset=ChaiVariety.objects.all(),
        label="Select Chai Variety",
        widget=forms.Select(
            attrs={
                "class": "w-1/2 p-2 border border-orange-500 rounded-lg focus:ring-2 focus:ring-orange-700 bg-orange-400 outline-none"
            }
        ),
        empty_label="Select category",
    )

from django import forms
from .models import TestData


class TestDataModelForm(forms.ModelForm):

    class Meta:
        model = TestData
        fields = ("number", "name", "price")


class TestDataForm(forms.Form):

    number = forms.IntegerField(
        label="number",
        min_value=0,
        required=True,
        error_messages={'required': 'numberが入力されていません'},
    )
    name = forms.CharField(
        label="name",
        max_length=128,
        required=True,
        error_messages={'required': 'nameが入力されていません'},
    )
    price = forms.IntegerField(
        label="price",
        min_value=0,
        required=True,
        error_messages={'required': 'priceが入力されていません'},
    )

from .models import MerchantRegisteModel,MerchantProductModel
from django import forms

class MerchantRegisteForm(forms.ModelForm):
    class Meta:
        model= MerchantRegisteModel
        fields="__all__"

class ProductDetailsSavingForm(forms.ModelForm):
    class Meta:
        model=MerchantProductModel
        fields='__all__'






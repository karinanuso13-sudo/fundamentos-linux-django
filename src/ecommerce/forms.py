from django import forms

from .models import ProductModel


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = [
            "name",
            "price",
            "description",
            "seller",
            "color",
            "product_dimensions",
            "short_description",
        ]
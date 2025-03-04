from django import forms
from .models import Product

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'product_id': 'Product ID',
            'name': 'Name',
            'sku': 'SKU',
            'price': 'Price',
            'quantity': 'Quantity',
            'supplier': 'Supplier'
        }

        widgets = {
            'product_id': forms.TextInput(attrs={'placeholder': 'e.g 1', 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'placeholder': 'e.g shirt', 'class': 'form-control'}),
            'sku': forms.TextInput(attrs={'placeholder': 'e.g 1234567890', 'class': 'form-control'}),
            'price': forms.TextInput(attrs={'placeholder': 'e.g 100', 'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'placeholder': 'e.g 10', 'class': 'form-control'}),
            'supplier': forms.TextInput(attrs={'placeholder': 'e.g Apple Inc.', 'class': 'form-control'}),
        }

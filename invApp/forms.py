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
            'supplier': 'Supplier',
        }
        widgets = {
            'product_id': forms.NumberInput(attrs={'placeholder':'1', 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'placeholder':'shirt', 'class': 'form-control'}),
            'sku': forms.TextInput(attrs={'placeholder':'S13H56G', 'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'placeholder':'200', 'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'placeholder':'10', 'class': 'form-control'}),
            'supplier': forms.TextInput(attrs={'placeholder':'Your Gadgets', 'class': 'form-control'}),
        }
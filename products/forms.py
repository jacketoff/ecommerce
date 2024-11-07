from django import forms
from .models import Products, Stock
from django.forms import ModelForm

SIZE_CHOICE = [
    ('small','small'),
    ('medium','medium'),
    ('large','large')
]

#this form is for single product page (when choosing weather to add product to cart)
class ProductForm(forms.Form):
    size = forms.ChoiceField(choices=SIZE_CHOICE,label='')
    quantity = forms.IntegerField(label='',initial=1)

#form for uploading products
class ProductModelForm(ModelForm):
    class Meta:
        model = Products
        fields = ['name','price','description','category','image']

class StockModelForm(ModelForm):
    class Meta:
        model = Stock  
        fields = ['small', 'medium', 'large']
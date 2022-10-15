from django import forms
from .models import Product, Customer, Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class CreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        
                


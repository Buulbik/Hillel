from django import forms
from apps.order.models import Cart, Order


class AddToCartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = '__all__'


class CreateOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"

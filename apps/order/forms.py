from django import forms
from apps.order.models import Cart


class AddToCartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = '__all__'


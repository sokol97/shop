from django import forms

# Генератор единиц товара
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)  # Количество единиц товара
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

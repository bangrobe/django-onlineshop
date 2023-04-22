from django import forms
from django.utils.translation import gettext_lazy as _
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1,21)]
'''
quantity: This allows the user to select a quantity between 1 and 20. You use a TypedChoiceField
field with coerce=int to convert the input into an integer.
• override: This allows you to indicate whether the quantity has to be added to any existing 
quantity in the cart for this product (False), or whether the existing quantity has to be overridden with the given quantity (True). You use a HiddenInput widget for this field, since you 
don’t want to display it to the user
'''

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int, label=_('Quantity'))
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class ProductAddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    #quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput(attrs={'class': 'form-control'}))
    #product_slug = forms.CharField(widget=forms.HiddenInput())
    
    

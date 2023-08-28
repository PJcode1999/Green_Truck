from django import forms
from .models import ShippingAddress


class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ['first_name','last_name','state','address_1','address_2','city','postpin','phone_number','email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'state': forms.Select(attrs={'class': 'form-select'}),
            'address_1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address Line 1'}),
            'address_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address Line 2'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'postpin': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Pin Code'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'})
        }
        
    def save(self, commit=True, user=None):
        instance = super(ShippingAddressForm, self).save(commit=False)
        
        if user:
            instance.user = user

        if commit:
            instance.save()

        return instance

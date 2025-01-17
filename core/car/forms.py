from django import forms
from .models import Car, Owner

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['owner', 'brand', 'model', 'year']

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['name', 'email']

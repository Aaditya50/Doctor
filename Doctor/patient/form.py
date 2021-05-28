from django.core import validators
from django import forms
from .models import User

class Patientinfo(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','contact','city']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'contact':forms.NumberInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
        }

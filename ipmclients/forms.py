from django import forms
from ipmclients.models import *
from ipmalpha.models import *

class AddClientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)    
    class Meta:
        model = Client
        fields = ['client_name', 'client_contact', 'client_telegram', 'client_phone', 'client_roletype', 'client_agreements']
        widgets = {
            'client_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 18rem'}),
            'client_contact': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 18rem'}),
            'client_telegram': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 18rem'}),
            'client_phone': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 18rem'}),
            'client_roletype': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 18rem'}),
            'client_agreements': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 18rem'}),
        }
        


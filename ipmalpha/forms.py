from django import forms
from ipmclients.models import *
from ipmalpha.models import *

class AddClientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)    
    class Meta:
        model = Client
        fields = ['client_name']
        widgets = {
            'client_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        

    
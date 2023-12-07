from django import forms
from ipmclients.models import *
from ipmalpha.models import *

class AddClientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        super(AddClientForm, self).__init__(*args, **kwargs)   
        self.fields['client_phone'].required = False
        self.fields['client_roletype'].required = False
        self.fields['client_telegram'].required = False
        self.fields['client_agreements'].required = False
    class Meta:
        model = Client
        fields = ['client_name', 'client_contact', 'client_telegram', 'client_phone', 'client_roletype', 'client_agreements']
        widgets = {
            'client_name': forms.TextInput(attrs={'class': 'form-control container-fluid', 'placeholder': 'Имя клиента*'}),
            'client_contact': forms.TextInput(attrs={'class': 'form-control container-fluid', 'placeholder': 'Контакт*'}),
            'client_telegram': forms.TextInput(attrs={'class': 'form-control container-fluid', 'placeholder': 'Телеграм'}),
            'client_phone': forms.TextInput(attrs={'class': 'form-control container-fluid', 'placeholder': 'Телефон'}),
            'client_roletype': forms.TextInput(attrs={'class': 'form-control container-fluid', 'placeholder': 'Тип клиента'}),
            'client_agreements': forms.TextInput(attrs={'class': 'form-control container-fluid', 'placeholder': 'Ссылка на договор'}),
        }

        


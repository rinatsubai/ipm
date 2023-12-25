from django import forms
from ipmclients.models import *
from ipmalpha.models import *
from finance.models import *

class AddTransactionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        super(AddTransactionForm, self).__init__(*args, **kwargs)   
    class Meta:
        model = Transaction
        fields = ['item', 'amount', 'flow', 'project', 'transaction_date']
        widgets = {
            'item': forms.TextInput(attrs={'class': 'input mb-5 is-bordered', 'placeholder': 'Статья расхода*'}),
            'amount': forms.NumberInput(attrs={'class': 'input  mb-5 is-bordered', 'placeholder': 'Сумма*'}),
            'flow': forms.Select(attrs={'class': 'mb-5', 'placeholder': 'Тип'}),
            'project': forms.Select(attrs={'class': 'mb-5', 'placeholder': 'Проект'}),
            'transaction_date':forms.TextInput(attrs={'class': 'input is-bordered mt-3', 'placeholder': 'Дата'})
        }

    
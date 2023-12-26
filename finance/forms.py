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

class FilterTransactionForm(forms.Form):    
    search = forms.CharField(max_length=512, required=False, widget=forms.TextInput(attrs={'class': 'input is-rounded', 'placeholder': 'Поиск транзакций'}))


class TransactionFilterForm(forms.Form):
    transaction_date_from = forms.DateField(required=False, widget=forms.TextInput(attrs={'class': 'input is-bordered is-inline mr-2', 'placeholder': 'Период, с'}))
    transaction_date_to = forms.DateField(required=False, widget=forms.TextInput(attrs={'class': 'input is-bordered is-inline', 'placeholder': 'Период, до'}))
     
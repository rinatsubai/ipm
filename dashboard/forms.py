from django import forms

class TransactionFilterForm(forms.Form):
    transaction_date_from = forms.DateField(required=False, widget=forms.TextInput(attrs={'class': 'input is-small is-bordered mt-3', 'placeholder': 'Период, с'}))
    
    transaction_date_to = forms.DateField(required=False, widget=forms.TextInput(attrs={'class': 'input is-small is-bordered my-3', 'placeholder': 'Период, до'}))
    # transaction_date_from = forms.DateField(required=False, widget=forms.SelectDateWidget(empty_label=("Год", "День", "Месяц"), attrs={'class': 'input my-2', 'placeholder': 'С'}))
    # transaction_date_to = forms.DateField(required=False, widget=forms.SelectDateWidget(empty_label=("Год", "День", "Месяц"), attrs={'placeholder': 'По'}))
    
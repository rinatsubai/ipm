from django.shortcuts import get_object_or_404, redirect, render
from finance.models import *
from finance.serializers import TransactionSerializer
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from finance.filters import TransactionFilter
import requests
import datetime
from datetime import date, datetime, timedelta
from rest_framework.renderers import TemplateHTMLRenderer
from finance.forms import AddTransactionForm
from django.contrib import messages
from django.views.generic import ListView, DetailView

class TransactionListAPIView(ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_class = TransactionFilter
    
class TransactionLastWeekAPIView(ListAPIView):
    serializer_class = TransactionSerializer
    def get_queryset(self):
        start_week = datetime.now()-timedelta(days=7)
        current_week = datetime.now()
        return Transaction.objects.filter(transaction_date__range=[start_week, current_week])
    
def finance_page(request):
    response = requests.get('http://127.0.0.1:8000/api/finance?ordering=-transaction_date')
    data = response.json()
    if request.method == 'POST':
        transaction = Transaction.objects.all()
        if request.method == 'POST':    
            addtransactionform = AddTransactionForm(request.POST)
            if addtransactionform.is_valid():
                successmessagetext = 'Добавлена транзакция.'
                try:
                    addtransactionform.save()
                   
                    print(addtransactionform.cleaned_data)
                    messages.success(request, 'Добавлена транзакция')
                    return redirect('finance_page')
                        # return HttpResponseRedirect(reverse(f'projects/{instance.pk}'))
                        # return redirect('clients')   
                        
                except:
                    AddTransactionForm.add_error(None, "Error")
                    addtransactionform = AddTransactionForm()
    else:
        addtransactionform = AddTransactionForm()
    return render(request, 'finance.html', {'data': data, 'addtransactionform': addtransactionform})

def finance_lw_page(request):
    response = requests.get('http://127.0.0.1:8000/api/financelw?ordering=-transaction_date')
    data = response.json
    if request.method == 'POST':
        transaction = Transaction.objects.all()
        if request.method == 'POST':    
            addtransactionform = AddTransactionForm(request.POST)
            if addtransactionform.is_valid():
                successmessagetext = 'Добавлена транзакция.'
                try:
                    addtransactionform.save()
                   
                    print(addtransactionform.cleaned_data)
                    messages.success(request, 'Добавлена транзакция')
                    return redirect('finance_page')
                        # return HttpResponseRedirect(reverse(f'projects/{instance.pk}'))
                        # return redirect('clients')   
                        
                except:
                    AddTransactionForm.add_error(None, "Error")
                    addtransactionform = AddTransactionForm()
    else:
        addtransactionform = AddTransactionForm()
    return render(request, 'finance.html', {'data': data, 'addtransactionform': addtransactionform})

class TransactionDetailView(DetailView):
    model = Transaction
    template_name = "transaction_view.html"
    def get_context_data(self, **kwargs):
        context = super(TransactionDetailView, self).get_context_data(**kwargs)
        context['transactionsall'] = Transaction.objects.all()

        return context


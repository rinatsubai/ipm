from django.shortcuts import get_object_or_404, redirect, render
from finance.models import *
from django.db.models import Q
from finance.serializers import TransactionSerializer
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from finance.filters import TransactionFilter
import requests
import datetime
from datetime import date, datetime, timedelta
from rest_framework.renderers import TemplateHTMLRenderer
from finance.forms import AddTransactionForm, FilterTransactionForm, TransactionFilterForm
from django.contrib import messages
from django.views.generic import ListView, DetailView

from ipmalpha.forms import FilterProjectForm

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
    
def finance_page_2(request):
    response = requests.get('http://127.0.0.1:8000/api/finance?ordering=-transaction_date')
    data = response.json()
    queryset = response
    if request.method == 'POST':
        transaction = Transaction.objects.all()
        if request.method == 'POST':    
            addtransactionform = AddTransactionForm(request.POST)
            if addtransactionform.is_valid():
                successmessagetext = 'Добавлена транзакция.'
                try:
                    addtransactionform.save()
                    messages.success(request, 'Добавлена транзакция')
                    return redirect('finance_page')
                        # return HttpResponseRedirect(reverse(f'projects/{instance.pk}'))
                        # return redirect('clients')   
                        
                except:
                    AddTransactionForm.add_error(None, "Error")
                    addtransactionform = AddTransactionForm()
    else:
        addtransactionform = AddTransactionForm()
    transactionfilterform = FilterTransactionForm
    search_result = request.GET.get('search')
    if search_result:
        queryset = queryset.filter(Q(item__icontains=search_result)| Q(project__icontains=search_result)| Q(project_product__icontains=search_result) | Q(project_client__client_name__icontains=search_result))
        data = queryset.json()
    return render(request, 'finance.html', {'data': data, 'addtransactionform': addtransactionform, 'transactionfilterform': transactionfilterform})

def finance_page(request):
    all_transactions = Transaction.objects.all()
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
        
    start_date=str(request.GET.get('transaction_date_from','1997-12-24'))
    end_date=str(request.GET.get('transaction_date_to','2099-12-24'))
    period = ''
    if start_date and end_date:
            all_transactions = Transaction.objects.filter(Q(transaction_date__gte=start_date), Q(transaction_date__lte=end_date),)
            period = 'с ' + start_date + ' по ' + end_date
            requested = True
    elif start_date:
            all_transactions = Transaction.objects.filter(Q(transaction_date__gte=start_date),)
            period = 'с ' + start_date + ' по сегодня'
            requested = True
    elif end_date:    
            all_transactions = Transaction.objects.filter(Q(transaction_date__lte=end_date),)
            period = 'по ' + end_date
            requested = True
    else:
            all_transactions = Transaction.objects.all()
            requested = False
    
    transactionfilterform = FilterTransactionForm
    transaction_filter_form = TransactionFilterForm
    search_result = request.GET.get('search')
    
    if search_result:
        all_transactions = all_transactions.filter(Q(item__icontains=search_result)| Q(project__project_name__icontains=search_result) |Q(amount__istartswith=search_result))
        transaction_filter_form = transaction_filter_form()
    return render(request, 'finance.html', {'data': all_transactions, 'addtransactionform': addtransactionform, 'transactionfilterform': transactionfilterform, 'search_result': search_result, 'transaction_filter_form': transaction_filter_form, 'period': period, 'requested': requested})

def finance_lw_page(request):
    response = requests.get('http://127.0.0.1:8000/api/financelw?ordering=-transaction_date')
    data = response.json
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
    transactionfilterform = FilterProjectForm
    return render(request, 'finance.html', {'data': data, 'addtransactionform': addtransactionform, 'transactionfilterform': transactionfilterform})

class TransactionDetailView(DetailView):
    model = Transaction
    template_name = "transaction_view.html"
    def get_context_data(self, **kwargs):
        context = super(TransactionDetailView, self).get_context_data(**kwargs)
        context['transactionsall'] = Transaction.objects.all()

        return context


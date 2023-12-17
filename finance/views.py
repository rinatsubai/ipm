from django.shortcuts import render
from finance.models import *
from finance.serializers import TransactionSerializer
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from finance.filters import TransactionFilter
import requests
import datetime
from datetime import date, datetime, timedelta

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
    return render(request, 'finance.html', {'data': data,})

def finance_lw_page(request):
    response = requests.get('http://127.0.0.1:8000/api/financelw?ordering=-transaction_date')
    data = response.json

    return render(request, 'finance.html', {'data': data,})
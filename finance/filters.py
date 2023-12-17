import django_filters
from finance.models import *

class TransactionFilter(django_filters.FilterSet):
    amount = django_filters.RangeFilter()
    flow = django_filters.LookupChoiceFilter()
    project = django_filters.LookupChoiceFilter()
    transaction_date = django_filters.DateTimeFromToRangeFilter()
    class Meta:
        model = Transaction
        fields = {
                    'id': ['exact'],
                    'item': ['icontains'], 
                  }
        


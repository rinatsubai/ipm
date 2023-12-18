import django_filters
from ipmclients.models import *

class ClientsAPIFilter(django_filters.FilterSet):
    class Meta:
        model = Client
        fields = {
                    'id': ['exact'],
                    'client_name': ['icontains'], 
                    'client_contact': ['icontains'],
                    'client_telegram': ['icontains'],
                    'client_phone': ['icontains'],
                    'client_roletype': ['icontains'],
                    'client_agreements': ['icontains'],
                    'client_active': ['icontains']
                  }
        


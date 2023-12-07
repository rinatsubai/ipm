import django_filters
from ipmalpha.models import *

class ProjectFilter(django_filters.FilterSet):
    project_sum = django_filters.RangeFilter()
    project_client = django_filters.LookupChoiceFilter()
    class Meta:
        model = Project
        fields = {
                    'id': ['exact'],
                    'project_name': ['icontains'], 
                     
                    'project_status': ['exact'], 
                    'project_product': ['icontains'],
                  }

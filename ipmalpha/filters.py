import django_filters
from ipmalpha.models import *

class ProjectFilter(django_filters.FilterSet):
    project_sum = django_filters.RangeFilter()
    class Meta:
        model = Project
        fields = {
                    'project_name': ['icontains'], 
                    'project_client': ['exact'],
                    'project_status': ['exact'], 
                    'project_product': ['icontains'], 
                  }
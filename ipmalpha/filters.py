import django_filters
from ipmalpha.models import *

class ProjectFilter(django_filters.FilterSet):
    class Meta:
        model = Project
        fields = {
            'project_name': ['icontains'], 
            'project_status': ['exact'], 
            'project_client': ['exact'], 
            'project_product': ['icontains'], 
            'project_sum': ['lt', 'gt']
                  }
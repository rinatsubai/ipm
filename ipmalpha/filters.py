import django_filters
from ipmalpha.models import *

class ProjectFilter(django_filters.FilterSet):
    class Meta:
        model = Project
        fields = ['project_name', 'project_status', 'project_client', 
                  'project_product', 'project_sum']
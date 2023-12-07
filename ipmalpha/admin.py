from django.contrib import admin
from ipmalpha.models import *

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'project_status', 'project_product', 'project_client', 'project_sum', 'project_created', 'project_finished')
    prepopulated_fields = {"slig": ("project_name",)}
    
admin.site.register(Status)
admin.site.register(Project)
from django.contrib import admin
from ipmalpha.models import *

# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'project_name', 'project_status', 'project_product', 'project_client', 'project_sum', 'project_created', 'project_finished')
    prepopulated_fields = {"slug": ("project_name", )}
    
@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'status_name', 'status_color')
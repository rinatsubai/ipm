from django.contrib import admin
from ipmalpha.models import *

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slig": ("project_name",)}
    
admin.site.register(Status)
admin.site.register(Project)
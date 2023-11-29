from django.contrib import admin
from ipmclients.models import *

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slig": ("client_name",)}
    
admin.site.register(Client)
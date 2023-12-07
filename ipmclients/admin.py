from django.contrib import admin
from ipmclients.models import *

# Register your models here.


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_name', 'client_contact', 'client_telegram', 'client_phone', 'client_roletype', 'client_agreements', 'client_active')
    prepopulated_fields = {"slig": ("client_name",)}
    
admin.site.register(Client)
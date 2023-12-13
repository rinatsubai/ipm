from django.contrib import admin
from ipmclients.models import *

# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_name', 'client_contact', 'client_telegram', 'client_phone', 'client_roletype', 'client_agreements', 'client_active',)
    list_editable = ('client_name', 'client_contact', 'client_telegram', 'client_phone', 'client_roletype', 'client_agreements', 'client_active',)

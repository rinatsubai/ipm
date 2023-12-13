from django.contrib import admin
from finance.models import Transaction

# Register your models here.

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'amount', 'flow', 'project', 'transaction_date')
    list_editable = ('item', 'amount', 'flow', 'project')
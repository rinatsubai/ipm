from rest_framework import serializers
from finance.models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            'id',
            'item',
            'amount',
            'flow',
            'project',
            'transaction_date',
        ]
        ordering_fields = ['transaction_date']
from rest_framework import serializers
from finance.models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    project = serializers.CharField(source='project.project_name')
    project_url = serializers.CharField(source='project.get_absolute_url')
    url = serializers.CharField(source='get_absolute_url')
    flow = serializers.CharField(source='get_flow_display')
    class Meta:
        model = Transaction
        fields = [
            'id',
            'item',
            'amount',
            'flow',
            'project',
            'transaction_date',
            'project_url',
            'url',
            
        ]
        ordering_fields = ['transaction_date']
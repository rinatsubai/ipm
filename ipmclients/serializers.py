from rest_framework import serializers
from ipmalpha.models import *
from ipmclients.models import *

class ProjectClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    content = ProjectClientSerializer(many=True, read_only=True)
    class Meta:
        model = Client
        fields = '__all__'
        

from rest_framework import serializers
from ipmalpha.models import *
from ipmclients.models import *

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        
class ClientProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
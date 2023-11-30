from rest_framework import serializers
from ipmalpha.models import Project, Status

class ProjectSerializer(serializers.ModelSerializer):
    project_status_name = serializers.CharField(source="project_status.status_name")
    class Meta:
        model = Project
        fields = (
            'project_name',
            'project_status',
            'project_product',
            'project_status_name',
            'project_sum',
        )
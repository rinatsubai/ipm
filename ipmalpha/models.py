from django.db import models
from ipmclients.models import *

# Create your models here.

class Status(models.Model):
    status_name = models.CharField(max_length=100)
    status_color = models.CharField(max_length=6, default='000000')
    def __str__(self):
        return self.status_name
    class Meta:
        ordering = ["id"]
        verbose_name = "status"
        verbose_name_plural = "statuses"
    pass

class Project(models.Model):
    project_name = models.CharField(max_length=512)
    def __str__(self):
        return self.project_name
    project_created = models.DateField(null=True)
    project_finished = models.DateField(null=True)
    project_status = models.ForeignKey(Status, on_delete=models.PROTECT, null=True)
    project_client = models.ForeignKey(Client, on_delete=models.PROTECT, null=True)
    project_product = models.CharField(max_length=512)
    project_sum = models.IntegerField(default=0)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True)
    
    class Meta:
        ordering = ["id"]
        verbose_name = "project"
        verbose_name_plural = "projects"
    pass
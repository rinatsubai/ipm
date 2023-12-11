from django.db import models
from django.utils import timezone
from ipmclients.models import *

# Create your models here.

class Status(models.Model):
    status_name = models.CharField(max_length=100)
    status_color = models.CharField(max_length=512, default='table-primary')
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
    project_created = models.DateTimeField(null=True, default=timezone.now)
    project_finished = models.DateTimeField(null=True)
    project_status = models.ForeignKey(Status, on_delete=models.PROTECT, null=True)
    project_client = models.ForeignKey(Client, on_delete=models.PROTECT, null=True, related_name='project')
    project_product = models.CharField(max_length=512)
    project_sum = models.IntegerField(default=0)
    # slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    
    def get_absolute_url(self):
        return reverse("project_detail", kwargs={'pk': self.pk})
    
    class Meta:
        ordering = ["pk"]
        verbose_name = "project"
        verbose_name_plural = "projects"
    pass
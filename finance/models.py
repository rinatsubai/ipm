from django.db import models
from django.urls import reverse
from ipmalpha.models import Project
from ipmclients.models import Client

# Create your models here.
class Transaction(models.Model):
    INCOME = 'INC'
    OUTCOME = 'OUT'
    SALARY = 'SAL'
    FLOW_CHOICES = [
        (INCOME, 'Income'),
        (OUTCOME, 'Outcome'),
        (SALARY, 'Salary'),
    ]
    
    item = models.CharField(max_length = 512)
    def __str__(self):
        return self.item
    amount = models.IntegerField()
    flow = models.CharField(max_length=3, choices=FLOW_CHOICES, default=INCOME)
    project = models.ForeignKey(Project, verbose_name=("Project"), on_delete=models.CASCADE, related_name='transaction')
    transaction_date = models.DateTimeField(blank=True, null=True)
    def get_absolute_url(self):
        return reverse("transaction_view", kwargs={'pk': self.pk})
    
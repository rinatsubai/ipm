from django.db import models
from ipmalpha.models import *
from django.urls import reverse
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Client(models.Model):
    client_name = models.CharField(max_length=512, unique = True)
    def __str__(self):
        return self.client_name
    client_contact = models.CharField(max_length=512, null=True)
    client_telegram = models.CharField(max_length=64, null=True)
    client_phone = PhoneNumberField(null=True, region="RU")
    client_roletype = models.CharField(max_length=512, null=True)
    client_agreements = models.CharField(max_length=1024, null=True)
    client_active = models.BooleanField(default=True)
    client_created = models.DateTimeField(null=True, default=timezone.now)
    client_updated = models.DateTimeField(null=True)
    client_closed = models.DateTimeField(null=True)
    
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.client_created = timezone.now()
        self.client_updated = timezone.now()
        return super(Client, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("client_view", kwargs={'pk': self.pk})
    
    def client_projects_sum(self, Project):
        qs2 = Client.objects.all()
        for c in qs2:
            c_id = c.id
            p = Project.objects.filter(project_client = c_id)
            return(p)
    
    
    class Meta:
        ordering = ["id"]
        verbose_name = "client"
        verbose_name_plural = "clients"
    pass
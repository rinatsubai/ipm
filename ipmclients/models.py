from django.db import models
from django.urls import reverse

# Create your models here.
class Client(models.Model):
    client_name = models.CharField(max_length=512)
    def __str__(self):
        return self.client_name
    client_contact = models.CharField(max_length=512, null=True)
    client_telegram = models.CharField(max_length=64, null=True)
    client_phone = models.CharField(max_length=11, null=True)
    client_roletype = models.CharField(max_length=512, null=True)
    client_agreements = models.CharField(max_length=1024, null=True)
    client_active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True)
    
    def get_absolute_url(self):
        return reverse("client", kwargs={"client_slug": self.slug})
    
    
    class Meta:
        ordering = ["id"]
        verbose_name = "client"
        verbose_name_plural = "clients"
    pass
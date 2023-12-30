from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    profileuser = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    profilename = models.CharField(max_length = 512, null=True, blank=True)
    first_name = User.first_name
    

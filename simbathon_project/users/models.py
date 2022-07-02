from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, default='', null=True)
    university = models.CharField(max_length=20, default='', null=True)
    major = models.CharField(max_length=20, default='', null=True)

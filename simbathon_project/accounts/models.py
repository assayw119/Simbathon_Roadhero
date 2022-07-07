from atexit import register
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=20, default='', null=True)
    university = models.CharField(max_length=20, default='', null=True)
    register = models.IntegerField(null=True)
    major = models.CharField(max_length=20, default='', null=True)
    major2 = models.CharField(max_length=20, default='', null=True)

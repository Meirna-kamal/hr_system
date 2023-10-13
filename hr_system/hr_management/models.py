from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    group = models.CharField(max_length=20, choices=[('HR', 'HR'), ('Normal Employee', 'Normal Employee')])
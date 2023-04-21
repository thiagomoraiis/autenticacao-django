from django.db import models
from django.contrib.auth.models import AbstractUser
#from django.db.models import signals

class CustomUser(AbstractUser):
    username = models.CharField(max_length=150,unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    idade = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True)
    data_nascimento = models.DateField(blank=True, null=True)

#    matricula = 
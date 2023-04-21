from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = models.CharField(max_length=150,unique=True)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=150, blank=False, null=False)
    idade = models.IntegerField()
    email = models.EmailField(blank=False, null=False)
    data_nascimento = models.DateField()
#    matricula = 
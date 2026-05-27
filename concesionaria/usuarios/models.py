from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UsuarioPersonalizado(AbstractUser):
    telefono = models.CharField(max_length=20, blank=True, null=True)  
    dni = models.CharField(max_length=10, blank=True,null=True)

    def __str__(self):
        return f"User: {self.username}"

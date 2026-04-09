from django.db import models

# Create your models here.
class Auto(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField()
    precio = models.DecimalField(decimal_places=2, max_digits=10)
    color = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.anio}) - ${self.precio}"

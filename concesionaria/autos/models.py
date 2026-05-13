from django.db import models


# Create your models here.
class Vendedor(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} contacto: {self.email} - {self.telefono}"

    class Meta:
        verbose_name = "Vendedor"
        verbose_name_plural = "Vendedores"


class Auto(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField()
    precio = models.DecimalField(decimal_places=2, max_digits=10)
    color = models.CharField(max_length=20)
    vendedor = models.ManyToManyField(
        Vendedor, default=None, blank=True, null=True, related_name="autos"
    )
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.anio}) - ${self.precio}"

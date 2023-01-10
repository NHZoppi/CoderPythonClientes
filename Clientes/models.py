from django.db import models
from django.utils import timezone
from decimal import Decimal

class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)

class Articulos(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.FloatField()
    descripcion = models.TextField()

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulos, on_delete=models.CASCADE)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.0))
    fecha = models.DateField(default=timezone.now)
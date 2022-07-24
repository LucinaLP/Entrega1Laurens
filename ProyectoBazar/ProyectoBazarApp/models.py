from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):
    
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to='avatar/', blank=True, null=True)


class Articulo(models.Model):      
    producto = models.CharField("Artículo", max_length=30)
    detalle = models.CharField("Detalle", max_length=30)
    cantidad = models.PositiveIntegerField("Cantidad")
    color = models.CharField("Color", max_length=15)
    precio = models.FloatField("Precio $")

class Nosotros(models.Model):
    direccion = models.CharField("Dirección", max_length=30)
    email = models.EmailField("Email")
    instagram = models.CharField("Instagram", max_length=30)
    
    
    class Meta:
        verbose_name_plural = "Nosotros"
    
class Servicios(models.Model):
    nombre = models.CharField("Servicio",max_length=30)
    
    class Meta:
        verbose_name_plural = "Servicios"
        
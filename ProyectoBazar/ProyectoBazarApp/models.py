from django.db import models
from phonenumbers import PhoneNumber


class Articulo(models.Model):      
    producto = models.CharField("Artículo", max_length=30)
    detalle = models.CharField("Detalle", max_length=30)
    cantidad = models.PositiveIntegerField("Cantidad")
    color = models.CharField("Color", max_length=15)
    precio = models.FloatField("Precio $")

class Nosotros(models.Model):
    direccion = models.CharField("Dirección", max_length=30)
    telefono = PhoneNumber()
    email = models.EmailField("Email")
    instagram = models.CharField("Instagram", max_length=30)
    
    
    class Meta:
        verbose_name_plural = "Nosotros"
    
class Servicios(models.Model):
    nombre = models.CharField("Servicio",max_length=30)
    
    class Meta:
        verbose_name_plural = "Servicios"
        
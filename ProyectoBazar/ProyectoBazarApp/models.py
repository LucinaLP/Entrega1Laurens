from django.db import models

class Articulo(models.Model):      
    producto = models.CharField("Artículo", max_length=30)
    detalle = models.CharField("Detalle", max_length=30)
    cantidad = models.PositiveIntegerField("Cantidad")
    color = models.CharField("Color", max_length=15)
    precio = models.FloatField("Precio $")
    

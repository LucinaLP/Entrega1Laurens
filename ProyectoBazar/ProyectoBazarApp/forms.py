from tabnanny import verbose
from django import forms

class NuevoArticulo(forms.Form):
    
    producto = forms.CharField(max_length=30, label= "Producto")
    cantidad = forms.IntegerField(min_value=0, label= "Cantidad")
    precio = forms.FloatField(min_value=0, label= "Precio")
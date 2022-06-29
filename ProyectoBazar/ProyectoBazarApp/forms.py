from tabnanny import verbose
from django import forms

class NuevoArticulo(forms.Form):
    
    producto = forms.CharField(max_length=30, )
    cantidad = forms.IntegerField(min_value=0, )
    precio = forms.FloatField(min_value=0, )
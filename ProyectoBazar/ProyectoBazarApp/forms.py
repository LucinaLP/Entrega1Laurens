from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NuevoArticulo(forms.Form):
    
    producto = forms.CharField(max_length=30, label= "Producto")
    cantidad = forms.IntegerField(min_value=0, label= "Cantidad")
    precio = forms.FloatField(min_value=0, label= "Precio")
    
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    
    first_name = forms.CharField(label="Nombre", required=False)
    last_name = forms.CharField(label="Apellido", required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
        
        help_texts = {k:"" for k in fields}
        
class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput, required=False)
    
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        
        #help_texts = {k:"" for k in fields}
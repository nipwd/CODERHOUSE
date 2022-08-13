from dataclasses import field
from pickle import TRUE
from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User

class EquiposForm(forms.Form):
    name=forms.CharField()
    base=forms.CharField()
    chief=forms.CharField()
    chassis=forms.CharField()
    powerunit=forms.CharField()

class PilotosForm(forms.Form):
    name=forms.CharField()
    team=forms.CharField()
    country=forms.CharField()
    podiums= forms.CharField()
    points= forms.CharField()
    Date=forms.DateField()

class PistasForm(forms.Form):
    name=forms.CharField()
    country=forms.CharField()
    length=forms.CharField()
    record=forms.CharField()

class UserRegisterForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)
    last_name = forms.CharField(label='Apellido')
    first_name = forms.CharField(label='Nombre')
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','last_name','first_name']
        help_texts = {k:"" for k in fields}


class Avatarform(forms.Form):
    imagen = forms.ImageField(label='imagen')

class BlogForm(forms.Form):
    titulo = forms.CharField()
    mensaje = forms.CharField()
    imagenBlog = forms.ImageField(label='imagenBlog')



class MessageForm(forms.Form):
    msg_content = forms.CharField(label='Escribi tu mensaje')

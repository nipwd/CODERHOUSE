"""CODER_HOUSE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from CODER_APP.views import *
from django.contrib.auth.views import LogoutView
from django.urls import path



urlpatterns = [
    path('',index, name='index'),
    path('pistas/', pistas_view, name='pistas'),
    path('pilotos/', pilotos_view, name='pilotos'),
    path('equipos/', Equipos_view, name='equipos'),
    path('teamForm/', equiposFormulario, name='equiposForm'),
    path('pistaForm/', pistasFormulario, name='pistaForm'),
    path('pilotoForm/', pilotosFormulario, name='pilotoForm'),
    path('buscar_equipos/', buscar_equipos, name='buscar_equipos'),
    path('buscar_pilotos/', buscar_pilotos, name='buscar_pilotos'),
    path('buscar_pistas/', buscar_pistas, name='buscar_pistas'),
    path('leerPistas/', LeerPistas, name="leerPistas"),
    path('eliminarPista/<pista_name>', eliminarPista, name="eliminarPista"),
    path('editarPista/<pista_name>', editarPista, name="editarPista"),
    path('login/', login_request, name='login'),
    path('register/', register, name= 'register'),
    path('logout/', LogoutView.as_view(template_name='templates/CODER_APP/logout.html'),name='logout'),
    path('Perfil/', Perfil, name="Perfil"),
    path('editarPerfil/', editarPerfil, name="editarPerfil"),
    path('agregarAvatar/', agregarAvatar, name='agregarAvatar'),

]


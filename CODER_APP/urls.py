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
    path('equipos/', Equipos_view, name='equipos'),
    path('blog/', Blog_view, name='blog'),
    ###pistas 
    path('pistaForm/', pistasFormulario, name='pistaForm'),
    path('buscar_pistas/', buscar_pistas, name='buscar_pistas'),
    path('eliminarPista/<pista_name>', eliminarPista, name="eliminarPista"),
    path('editarPista/<pista_name>', editarPista, name="editarPista"),
    path('leerPistas/', LeerPistas, name="leerPistas"),
    ## fin pistas
    ### equipo
    path('teamForm/', equiposFormulario, name='equiposForm'),
    path('buscar_equipos/', buscar_equipos, name='buscar_equipos'),
    path('eliminarEquipos/<equipo_name>', eliminarEquipos, name="eliminarEquipos"),
    path('editarEquipo/<equipo_name>', editarEquipos, name="editarEquipo"),
    path('leerEquipos/', LeerEquipos, name="leerEquipos"),
    ## fin equipos
    ### pilotos
    path('pilotoForm/', pilotosFormulario, name='pilotoForm'),
    path('buscar_pilotos/', buscar_pilotos, name='buscar_pilotos'),
    path('eliminarPiloto/<piloto_name>', eliminarPilotos, name="eliminarPiloto"),
    path('editarPiloto/<piloto_name>', editarPilotos, name="editarPiloto"),
    path('leerPilotos/', LeerPilotos, name="leerPilotos"),
    ## fin pilotos
      ### blog
    path('blogForm/', blogFormulario, name='blogForm'),
    path('buscar_blog/', buscar_blog, name='buscar_blog'),
    path('eliminarblog/<blog_titulo>', eliminarblog, name="eliminarblog"),
    path('editarblog/<blog_titulo>', editarblog, name="editarblog"),
    path('LeerBlog/', LeerBlog, name="LeerBlog"),
    path('verblog/<blog_titulo>', verblog, name="verblog"),
    ## fin blog
    #user
    path('login/', login_request, name='login'),
    path('register/', register, name= 'register'),
    path('logout/', LogoutView.as_view(template_name='templates/CODER_APP/logout.html'),name='logout'),
    path('Perfil/', Perfil, name="Perfil"),
    path('editarPerfil/', editarPerfil, name="editarPerfil"),
    path('agregarAvatar/', agregarAvatar, name='agregarAvatar'),

]


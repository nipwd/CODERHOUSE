from tkinter import E
from wsgiref.util import request_uri
from django.shortcuts import render
from django.template import Context, Template
from CODER_APP.models import *
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from CODER_APP.forms import *




# Create your views here.
def index(request):
    return render(request,'templates/index.html')

def schedule(request):
    return render(request,'templates/CODER_APP/schedule/schedule.html')

def standings(request):
    return render(request,'templates/CODER_APP/standings/standings.html')

def drivers(request):
    return render(request,'templates/CODER_APP/drivers/drivers.html')

def teams(request):
    return render(request,'templates/CODER_APP/teams/teams.html')


def equiposFormulario(request):
    if (request.method == "POST"):
        form= EquiposForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre= info["name"]
            origen= info["base"]
            jefe= info["chief"]
            chasis= info["chassis"]
            unidadPotencia= info["powerunit"]
            equipo= Equipos(name=nombre,base=origen,chief=jefe,chassis=chasis,powerunit=unidadPotencia)
            equipo.save()
            return render(request,'templates/index.html')
    else:
        form= EquiposForm()
        return render(request,'templates/CODER_APP/formularios/equipos_form.html', {'formulario': form})

def pilotosFormulario(request):
    return render(request,'templates/CODER_APP/formularios/pilotos_form.html')


def pistasFormulario(request):
    return render(request,'templates/CODER_APP/formularios/pistas_form.html')

def buscarEquipos(request):
    return render(request,'templates/CODER_APP/busqueda/buscarEquipos.html')

def buscar(request):
    if request.GET['equipo']:
        equipo= request.GET['equipo']
        equipo= Equipos.objects.filter(equipo__icontains=equipo)  ###
        return render(request,'templates/CODER_APP/busqueda/resultadosBusqueda.html', {"equipos":equipo})
    else:
        return render(request,'templates/CODER_APP/busqueda/buscarEquipos.html')








def login_request(request):
    if request.method == 'POST':
        form= AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password') 
            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request,user)
                return render(request,'templates/index.html',{"message":f"bienvenido{usuario}"})
            else:
                return render(request,'templates/index.html',{"message":"ERROR, datos incorrectos"})
        else:
            return render(request,'templates/index.html',{"message":"ERROR, formulario erroneo"})
    form = AuthenticationForm()
    return render(request,'templates/CODER_APP/login.html', {'form':form})



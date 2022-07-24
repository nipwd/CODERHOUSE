from unicodedata import name
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


def pistas_view(request):
    return render(request,'templates/CODER_APP/pistas/pistas.html')

def pilotos_view(request):
    return render(request,'templates/CODER_APP/pilotos/pilotos.html')

def Equipos_view(request):
    return render(request,'templates/CODER_APP/equipos/equipos.html')


### forms
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
    if (request.method == "POST"):
        form= EquiposForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            name= info["name"]
            team= info["team"]
            country= info["country"]
            podiums= info["podiums"]
            points= info["points"]
            Date= info["Date"]
            pilotos= Pilotos(name=name,team=team,country=country,podiums=podiums,points=points,Date=Date)
            pilotos.save()
            return render(request,'templates/index.html')
    else:
        form= EquiposForm()
        return render(request,'templates/CODER_APP/formularios/pilotos_form.html', {'formulario': form})

def pistasFormulario(request):
    if (request.method == "POST"):
        form= EquiposForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            name= info["name"]
            country= info["country"]
            laps= info["laps"]
            length= info["length"]
            record= info["record"]
            pistas= Pistas(name=name,country=country,laps=laps,length=length,record=record)
            pistas.save()
            return render(request,'templates/index.html')
    else:
        form= EquiposForm()
        return render(request,'templates/CODER_APP/formularios/pistas_form.html', {'formulario': form})


### busqueda


def buscar_equipos(request):
    if request.GET['equipos']:
        equipo= request.GET['equipos']
        equipo= Equipos.objects.filter(name__icontains=equipo)  ###
        return render(request,'templates/CODER_APP/busqueda/resultadosBusqueda_equipo.html', {"equipos":equipo})
    else:
        return render(request,'templates/CODER_APP/equipos/equipos.html')



def buscar_pilotos(request):
    if request.GET['pilotos']:
        piloto= request.GET['pilotos']
        piloto= Equipos.objects.filter(name__icontains=piloto)  ###
        return render(request,'templates/CODER_APP/busqueda/resultadosBusqueda_pilotos.html', {"piloto":piloto})
    else:
        return render(request,'templates/CODER_APP/pilotos/pilotos.html')



def buscar_pistas(request):
    if request.GET['pistas']:
        pistas= request.GET['pistas']
        pistas= Equipos.objects.filter(name__icontains=pistas)  ###
        return render(request,'templates/CODER_APP/busqueda/resultadosBusqueda_pistas.html', {"pistas":pistas})
    else:
        return render(request,'templates/CODER_APP/pistas/pistas.html')




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
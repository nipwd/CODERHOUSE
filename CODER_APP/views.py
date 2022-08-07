from unicodedata import name
from urllib import request
from django.shortcuts import render
from django.template import Context, Template
from CODER_APP.models import *
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from CODER_APP.forms import *
from CODER_APP.forms import Avatarform
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



# Create your views here.
def index(request):
    return render(request,'templates/index.html')

@login_required
def pistas_view(request):
    pistas= Pistas.objects.all()
    return render(request,'templates/CODER_APP/pistas/pistas.html', {"pistas":pistas})

@login_required
def pilotos_view(request):
    return render(request,'templates/CODER_APP/pilotos/pilotos.html')

@login_required
def Equipos_view(request):
    return render(request,'templates/CODER_APP/equipos/equipos.html')


### forms
@login_required
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

@login_required
def pilotosFormulario(request):
    if (request.method == "POST"):
        form= PilotosForm(request.POST)
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
        form= PilotosForm()
        return render(request,'templates/CODER_APP/formularios/pilotos_form.html', {'formulario': form})

@login_required
def pistasFormulario(request):
    if (request.method == "POST"):
        form= PistasForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            name= info["name"]
            country= info["country"]
            length= info["length"]
            record= info["record"]
            pistas= Pistas(name=name,country=country,length=length,record=record)
            pistas.save()
            return render(request,'templates/index.html')
    else:
        form= PistasForm()
        return render(request,'templates/CODER_APP/formularios/pistas_form.html', {'formulario': form})


### busqueda

@login_required
def buscar_equipos(request):
    if request.GET['equipos']:
        equipo= request.GET['equipos']
        equipo= Equipos.objects.filter(name__icontains=equipo)  ###
        return render(request,'templates/CODER_APP/busqueda/resultadosBusqueda_equipo.html', {"equipos":equipo})
    else:
        return render(request,'templates/CODER_APP/equipos/equipos.html')


@login_required
def buscar_pilotos(request):
    if request.GET['pilotos']:
        piloto= request.GET['pilotos']
        piloto= Pilotos.objects.filter(name__icontains=piloto)  ###
        return render(request,'templates/CODER_APP/busqueda/resultadosBusqueda_pilotos.html', {"piloto":piloto})
    else:
        return render(request,'templates/CODER_APP/pilotos/pilotos.html')


@login_required
def buscar_pistas(request):
    if request.GET['pistas']:
        pistas= request.GET['pistas']
        pistas= Pistas.objects.filter(name__icontains=pistas)  ###
        return render(request,'templates/CODER_APP/busqueda/resultadosBusqueda_pistas.html', {"pistas":pistas})
    else:
        return render(request,'templates/CODER_APP/pistas/pistas.html')


#### LEER
@login_required
def LeerPistas(request):
    pistas= Pistas.objects.all()
    return render(request, "templates/CODER_APP/lectura/leerPistas.html", {"pistas":pistas})
####borrar post duplicado a clase pilotos / equipos



#### eliminar 
@login_required
def eliminarPista(request, pista_name):
    pista = Pistas.objects.get(name=pista_name)
    pista.delete()
    pistas= Pistas.objects.all()
    return render(request, 'templates/CODER_APP/pistas/pistas.html', {"pistas":pistas})

####duplicar a clase pilotos / equipos

### editar
@login_required
def editarPista(request,pista_name):
    pista= Pistas.objects.get(name=pista_name)
    if request.method == 'POST':
        form = PistasForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data()
            pista.name= info["name"]
            pista.country= info["country"]
            pista.length= info["length"]
            pista.record= info["record"]
            pista.save()
            return render(request,'templates/index.html')
    else:
        form= PistasForm(initial={"name":pista.name,"country":pista.country,"length":pista.length,"record":pista.record})
    return render(request,'templates/CODER_APP/pistas/editar_pista.html', {"formulario": form,"pista_name":pista_name})


@login_required
def editarPerfil(request):
    usuario = request.user

    if request.method == 'POST':
        formulario = UserEditForm(request.POST, instance = usuario)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save() 
            return render(request,'templates/index.html',{'usuario':usuario, 'mensaje':'perfil editado correctamente'})
    else:
        formulario = UserEditForm(instance = usuario)
    return render(request,'templates/CODER_APP/editarperfil.html', {'formulario':formulario, 'usuario':usuario.username})



def agregarAvatar(request):
    if request.method == 'POST':
        formulario=Avatarform(request.POST, request.FILES)
        if formulario.is_valid():
            try:
                avatarViejo=Avatar.objects.get(user=request.user)
                if(avatarViejo.imagen):
                    avatarViejo.delete()
                    avatar=Avatar(user=request.user, imagen=formulario.cleaned_data['imagen'])
                avatar.save()
                return render(request, 'templates/index.html', {'usuario':request.user, 'mensaje':'AVATAR AGREGADO EXITOSAMENTE'})
            except:
                avatar=Avatar(user=request.user, imagen=formulario.cleaned_data['imagen'])
                avatar.save()
                return render(request, 'templates/index.html', {'usuario':request.user, 'mensaje':'AVATAR AGREGADO EXITOSAMENTE'})
    else:
        formulario= Avatarform()
    return render(request, 'templates/CODER_APP/agregar_avatar.html', {'formulario':formulario, 'usuario':request.user})





##############

def login_request(request):
    if request.method == 'POST':
        form= AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password') 
            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request,user)
                return render(request,'templates/index.html',{"form":form, "mensaje": f"Bienvenido {usuario}"})
            else:
                return render(request,'templates/CODER_APP/login.html',{"form":form, "mensaje": f"Usuario o clave incorrectos"})
        
        else:
            return render(request,'templates/CODER_APP/login.html',{"form":form, "mensaje": f"Formulario invalido"})
        
    else:
        form = AuthenticationForm()
        return render(request,'templates/CODER_APP/login.html', {'form':form})



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request,'templates/index.html',{"form":form, "mensaje": f"Usuario Creado {username}"})
    else:
        form = UserRegisterForm()
    return render(request, 'templates/CODER_APP/register.html', {'form': form})


def Perfil(request):
    return render(request,'templates/CODER_APP/Perfil.html') 
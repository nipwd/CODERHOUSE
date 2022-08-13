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

coments = []


def mostrar_avatar(request):
    global imagen_avatar
    try:
        imagen_avatar=Avatar.objects.filter(user= request.user.id)[0].imagen.url
        return imagen_avatar
    except:
        imagen_avatar = 'media/avatares/avatarPorDefecto.png'
        return imagen_avatar



# Create your views here.

def index(request):
    mostrar_avatar(request)
    imagen_avatar
    return render(request,'templates/index.html',{"imagen_avatar":imagen_avatar})


def about(request):
    mostrar_avatar(request)
    imagen_avatar
    return render(request,'templates/CODER_APP/about.html',{"imagen_avatar":imagen_avatar})


@login_required
def pistas_view(request):
    mostrar_avatar(request)
    imagen_avatar
    pistas= Pistas.objects.all()
    return render(request,'templates/CODER_APP/pistas/pistas.html', {"pistas":pistas,"imagen_avatar":imagen_avatar})

@login_required
def pilotos_view(request):
    mostrar_avatar(request)
    imagen_avatar
    pilotos= Pilotos.objects.all()
    return render(request,'templates/CODER_APP/pilotos/pilotos.html', {"pilotos":pilotos,"imagen_avatar":imagen_avatar})

@login_required
def Equipos_view(request):
    mostrar_avatar(request)
    imagen_avatar
    equipos= Equipos.objects.all()
    return render(request,'templates/CODER_APP/equipos/equipos.html',{"equipos":equipos,"imagen_avatar":imagen_avatar})

@login_required
def Blog_view(request):
    mostrar_avatar(request)
    imagen_avatar
    blog= Blog.objects.all()
    credor = Blog.user
    return render(request,'templates/CODER_APP/blog/blog.html',{"credor":credor,"blog":blog,"imagen_avatar":imagen_avatar})

def Perfil(request):
    mostrar_avatar(request)
    imagen_avatar
    return render(request,'templates/CODER_APP/Perfil.html',{"imagen_avatar":imagen_avatar}) 



######################################################################## pistas
### form
@login_required
def pistasFormulario(request):
    mostrar_avatar(request)
    imagen_avatar
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
        return render(request,'templates/CODER_APP/formularios/pistas_form.html', {'formulario': form,"imagen_avatar":imagen_avatar})


#buscar
@login_required
def buscar_pistas(request):
    mostrar_avatar(request)
    imagen_avatar
    if request.GET['pistas']:
        pistas= request.GET['pistas']
        pistas= Pistas.objects.filter(name__icontains=pistas)  ###
        return render(request,'templates/CODER_APP/busqueda/resultadosBusqueda_pistas.html', {"pistas":pistas,"imagen_avatar":imagen_avatar})
    else:
        return render(request,'templates/CODER_APP/pistas/pistas.html',{"imagen_avatar":imagen_avatar})


#eliminar
@login_required
def eliminarPista(request, pista_name):
    mostrar_avatar(request)
    imagen_avatar
    pista = Pistas.objects.get(name=pista_name)
    pista.delete()
    pistas= Pistas.objects.all()
    return render(request, 'templates/CODER_APP/pistas/pistas.html', {"pistas":pistas,"imagen_avatar":imagen_avatar})


### editar
@login_required
def editarPista(request,pista_name):
    mostrar_avatar(request)
    imagen_avatar
    pista= Pistas.objects.get(name=pista_name)
    if request.method == 'POST':
        form = PistasForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            pista.name= info["name"]
            pista.country= info["country"]
            pista.length= info["length"]
            pista.record= info["record"]
            pista.save()
            return render(request,'templates/index.html',{"imagen_avatar":imagen_avatar})
    else:
        form= PistasForm(initial={"name":pista.name,"country":pista.country,"length":pista.length,"record":pista.record,"imagen_avatar":imagen_avatar})
    return render(request,'templates/CODER_APP/pistas/editar_pista.html', {"formulario": form,"pista_name":pista_name,"imagen_avatar":imagen_avatar})


#### LEER
@login_required
def LeerPistas(request):
    mostrar_avatar(request)
    imagen_avatar
    pistas= Pistas.objects.all()
    return render(request, "templates/CODER_APP/lectura/leerPistas.html", {"pistas":pistas,"imagen_avatar":imagen_avatar})

#############################fin pistas



######################################################################## pilotos
### form
@login_required
def pilotosFormulario(request):
    mostrar_avatar(request)
    imagen_avatar
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
    return render(request,'templates/CODER_APP/formularios/pilotos_form.html', {'formulario': form,"imagen_avatar":imagen_avatar})


#buscar
@login_required
def buscar_pilotos(request):
    mostrar_avatar(request)
    imagen_avatar
    if request.GET['pilotos']:
        pilotos= request.GET['pilotos']
        pilotos= Pilotos.objects.filter(name__icontains=pilotos)  ###
        return render(request,'templates/CODER_APP/busqueda/resultadosBusqueda_pilotos.html', {"pilotos":pilotos,"imagen_avatar":imagen_avatar})
    else:
        return render(request,'templates/CODER_APP/pilotos/pilotos.html',{"imagen_avatar":imagen_avatar})


#eliminar
@login_required
def eliminarPilotos(request, piloto_name):
    mostrar_avatar(request)
    imagen_avatar
    piloto = Pilotos.objects.get(name=piloto_name)
    piloto.delete()
    piloto= Pilotos.objects.all()
    return render(request, 'templates/CODER_APP/pistas/pistas.html', {"piloto":piloto,"imagen_avatar":imagen_avatar})


### editar
@login_required
def editarPilotos(request,piloto_name):
    mostrar_avatar(request)
    imagen_avatar
    piloto= Pilotos.objects.get(name=piloto_name)
    if request.method == 'POST':
        form = PilotosForm(request.POST)
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
            return render(request,'templates/index.html',{"imagen_avatar":imagen_avatar})
    else:
        form= PilotosForm(initial={"name":piloto.name,"team":piloto.country,"country":piloto.length,"podiums":piloto.record,"points":piloto.points,"Date":piloto.Date,"imagen_avatar":imagen_avatar})
    return render(request,'templates/CODER_APP/pilotos/editar_pilotos.html', {"formulario": form,"piloto_name":piloto_name,"imagen_avatar":imagen_avatar})


#### LEER
@login_required
def LeerPilotos(request):
    mostrar_avatar(request)
    imagen_avatar
    pilotos= Pilotos.objects.all()
    return render(request, "templates/CODER_APP/lectura/LeerPilotos.html", {"pilotos":pilotos,"imagen_avatar":imagen_avatar})

#############################fin pilotos

######################################################################## equipos
### form
@login_required
def equiposFormulario(request):
    mostrar_avatar(request)
    imagen_avatar
    if (request.method == "POST"):
        form= EquiposForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            name= info["name"]
            base= info["base"]
            chief= info["chief"]
            chassis= info["powerunit"]
            pistas= Equipos(name=name,base=base,chief=chief,chassis=chassis)
            pistas.save()
            return render(request,'templates/index.html')
    else:
        form= EquiposForm()
        return render(request,'templates/CODER_APP/formularios/equipos_form.html', {'formulario': form,"imagen_avatar":imagen_avatar})


#buscar
@login_required
def buscar_equipos(request):
    mostrar_avatar(request)
    imagen_avatar
    if request.GET['equipos']:
        equipos= request.GET['equipos']
        equipos= Equipos.objects.filter(name__icontains=equipos)  ###
        return render(request,'templates/CODER_APP/busqueda/resultadosBusqueda_equipo.html', {"equipos":equipos,"imagen_avatar":imagen_avatar})
    else:
        return render(request,'templates/CODER_APP/equipos/equipos.html',{"imagen_avatar":imagen_avatar})

#eliminar
@login_required
def eliminarEquipos(request, equipo_name):
    mostrar_avatar(request)
    imagen_avatar
    equipo = Equipos.objects.get(name=equipo_name)
    equipo.delete()
    equipos= Equipos.objects.all()
    return render(request, 'templates/CODER_APP/equipos/equipos.html', {"equipos":equipos,"imagen_avatar":imagen_avatar})


### editar
@login_required
def editarEquipos(request,equipo_name):
    mostrar_avatar(request)
    imagen_avatar
    equipo= Equipos.objects.get(name=equipo_name)
    if request.method == 'POST':
        form = EquiposForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            equipo.name= info["name"]
            equipo.base= info["base"]
            equipo.chief= info["chief"]
            equipo.chassis= info["chassis"]
            equipo.powerunit= info["powerunit"]
            equipo.save()
            return render(request,'templates/index.html',{"imagen_avatar":imagen_avatar})
    else:
        form= EquiposForm(initial={"name":equipo.name,"base":equipo.base,"chief":equipo.chief,"chassis":equipo.chassis,"powerunit":equipo.powerunit,"imagen_avatar":imagen_avatar})
    return render(request,'templates/CODER_APP/equipos/editar_equipos.html', {"formulario": form,"equipo_name":equipo_name,"imagen_avatar":imagen_avatar})


#### LEER
@login_required
def LeerEquipos(request):
    mostrar_avatar(request)
    imagen_avatar
    equipos= Equipos.objects.all()
    return render(request, "templates/CODER_APP/lectura/leerPistas.html", {"equipos":equipos,"imagen_avatar":imagen_avatar})

############################# fin equipos

######################################################################## blog
### form
@login_required
@login_required
def blogFormulario(request):
    mostrar_avatar(request)  
    imagen_avatar
    if (request.method == "POST"):
        form= BlogForm(request.POST, request.FILES)
        if form.is_valid():
            info = form.cleaned_data
            titulo= info["titulo"]
            mensaje= info["mensaje"]
            imagenBlog = info['imagenBlog']
            usuario = request.user
            blog= Blog(user=usuario,titulo=titulo,mensaje=mensaje,imagenBlog=imagenBlog)
            blog.save()
            return render(request,'templates/index.html')
    else:
        form= BlogForm()
    return render(request,'templates/CODER_APP/formularios/blog_form.html', {'formulario': form,"imagen_avatar":imagen_avatar})

#buscar
@login_required
def buscar_blog(request):
    mostrar_avatar(request)
    imagen_avatar
    if request.GET['blog']:
        blog= request.GET['blog']
        blog= Blog.objects.filter(titulo__icontains=blog)  ###
        return render(request,'templates/CODER_APP/busqueda/resultadosBusqueda_blog.html', {"blog":blog,"imagen_avatar":imagen_avatar})
    else:
        return render(request,'templates/CODER_APP/blog/blog.html',{"imagen_avatar":imagen_avatar})


#eliminar
@login_required
def eliminarblog(request, blog_titulo):
    mostrar_avatar(request)
    imagen_avatar
    blog = Blog.objects.get(titulo=blog_titulo)
    blog.delete()
    blog= Blog.objects.all()
    return render(request, 'templates/CODER_APP/blog/blog.html', {"blog":blog,"imagen_avatar":imagen_avatar})


### editar
@login_required
def editarblog(request,blog_titulo):
    mostrar_avatar(request)
    imagen_avatar
    blog= Blog.objects.get(titulo=blog_titulo)
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            blog.titulo= info["titulo"]
            blog.mensaje= info["mensaje"]
            blog.save()
            return render(request,'templates/index.html',{"imagen_avatar":imagen_avatar})
    else:
        form= BlogForm(initial={"titulo":blog.titulo,"mensaje":blog.mensaje,"imagen_avatar":imagen_avatar})
    return render(request,'templates/CODER_APP/blog/editar_blog.html', {"formulario": form,"blog_titulo":blog_titulo,"imagen_avatar":imagen_avatar})


#### LEER
@login_required
def LeerBlog(request):
    mostrar_avatar(request)
    imagen_avatar
    blog= Blog.objects.all()
    return render(request, "templates/CODER_APP/lectura/leerBlog.html", {"blog":blog,"imagen_avatar":imagen_avatar})






### editar
@login_required
def verblog(request,blog_titulo):
    mostrar_avatar(request)
    imagen_avatar
    blog= Blog.objects.get(titulo=blog_titulo)

   
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.cleaned_data        
    else:
        form= BlogForm(initial={"imagenBlog":blog.imagenBlog,"fecha_post":blog.fecha_post,"titulo":blog.titulo,"mensaje":blog.mensaje,"imagen_avatar":imagen_avatar})
    return render(request,'templates/CODER_APP/blog/ver_blog.html', {"creador":blog.user,"fecha_post":blog.fecha_post,"formulario": form,"blog_titulo":blog_titulo,"mensaje":blog.mensaje,"imagenBlog":blog.imagenBlog,"imagen_avatar":imagen_avatar})
#############################fin blog

############################################################### usuario
def agregarAvatar(request):
    mostrar_avatar(request)
    imagen_avatar
    if request.method == 'POST':
        formulario=Avatarform(request.POST, request.FILES)
        if formulario.is_valid():
            try:
                avatarViejo=Avatar.objects.get(user=request.user)
                if(avatarViejo.imagen):
                    avatarViejo.delete()
                    avatar=Avatar(user=request.user, imagen=formulario.cleaned_data['imagen'])
                avatar.save()
                return render(request, 'templates/index.html', {'usuario':request.user, 'mensaje':'AVATAR AGREGADO EXITOSAMENTE',"imagen_avatar":imagen_avatar})
            except:
                avatar=Avatar(user=request.user, imagen=formulario.cleaned_data['imagen',"imagen_avatar":imagen_avatar])
                avatar.save()
                return render(request, 'templates/index.html', {'usuario':request.user, 'mensaje':'AVATAR AGREGADO EXITOSAMENTE',"imagen_avatar":imagen_avatar})
    else:
        formulario= Avatarform()
    return render(request, 'templates/CODER_APP/agregar_avatar.html', {'formulario':formulario, 'usuario':request.user,"imagen_avatar":imagen_avatar})



@login_required
def editarPerfil(request):
    usuario = request.user
    mostrar_avatar(request)
    imagen_avatar
    if request.method == 'POST':
        formulario = UserEditForm(request.POST, instance = usuario)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save() 
            return render(request,'templates/index.html',{'usuario':usuario, 'mensaje':'perfil editado correctamente',"imagen_avatar":imagen_avatar})
    else:
        formulario = UserEditForm(instance = usuario)
    return render(request,'templates/CODER_APP/editarperfil.html', {'formulario':formulario, 'usuario':usuario.username,"imagen_avatar":imagen_avatar})



def login_request(request):
    mostrar_avatar(request)
    imagen_avatar
    if request.method == 'POST':
        form= AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password') 
            user = authenticate(username=usuario, password=contra)
            if user is not None:
                login(request,user)
                return render(request,'templates/index.html',{"form":form, "mensaje": f"Bienvenido {usuario}","imagen_avatar":imagen_avatar})
            else:
                return render(request,'templates/CODER_APP/login.html',{"form":form, "mensaje": f"Usuario o clave incorrectos","imagen_avatar":imagen_avatar})
        
        else:
            return render(request,'templates/CODER_APP/login.html',{"form":form, "mensaje": f"Formulario invalido","imagen_avatar":imagen_avatar})
        
    else:
        form = AuthenticationForm()
        return render(request,'templates/CODER_APP/login.html', {'form':form,"imagen_avatar":imagen_avatar})



def register(request):
    mostrar_avatar(request)
    imagen_avatar
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request,'templates/index.html',{"form":form, "mensaje": f"Usuario Creado {username}","imagen_avatar":imagen_avatar})
    else:
        form = UserRegisterForm()
    return render(request, 'templates/CODER_APP/register.html', {'form': form,"imagen_avatar":imagen_avatar})




#######corregir formulario ya que no carga , discriminar por usuario en html
def mensajes(request):
    mostrar_avatar(request)
    imagen_avatar
    usuario = request.user
    if (request.method == "POST"):
        form= MessageForm(request.POST)
        if form.is_valid():
         
            msg = Message.objects.all()

            return render(request,'templates/index.html',{'msg':msg})
    else:
        form= MessageForm()
        msg = Message.objects.all()
    return render(request,'templates/CODER_APP/formularios/mensaje_form.html', {'msg':msg,'formulario': form,"imagen_avatar":imagen_avatar})

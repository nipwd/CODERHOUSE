from calendar import c
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pilotos(models.Model):
    name=models.CharField(max_length=50)
    team=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    podiums= models.IntegerField()
    points= models.IntegerField()
    Date=models.DateField()
    def __str__(self):
        return self.name+" corre para "+self.team+", es de  "+self.country+", podios:  "+str(self.podiums)+", puntos: "+str(self.points)+", fecha nacimiento: "+str(self.Date)


class Equipos(models.Model):
    name=models.CharField(max_length=50)
    base=models.CharField(max_length=50)
    chief=models.CharField(max_length=50)
    chassis=models.CharField(max_length=50)
    powerunit=models.CharField(max_length=50)
    def __str__(self):
        return self.name+" , tiene su base en "+self.base+", el jefe de equipo es: "+self.chief+", el chasis de este año se llama: "+self.chassis+", suministrador de motores: "+self.powerunit


class Pistas(models.Model):
    name=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    length=models.FloatField(max_length=50)
    record=models.FloatField(max_length=50)
    def __str__(self):
        return self.name+", Country: "+self.country+", Circuit Length:  "+str(self.length)+" km, "+"Record: "+str(self.record)



class Avatar(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null= True, blank=True)
    


class Blog(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    mensaje =models.TextField()
    fecha_post = models.DateTimeField(auto_now_add=True,null=True)
    imagenBlog = models.ImageField(upload_to="blog", null= True, blank=True)
    def __str__(self):
        return str(self.user)+str(self.titulo)+str(self.mensaje)+str(self.fecha_post)


class Message(models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE)
    reciever = models.CharField(max_length=50)
    msg_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return str(self.sender)+str(self.reciever)+str(self.msg_content)+str(self.created_at)
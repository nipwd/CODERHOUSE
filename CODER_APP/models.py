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
        return self.name+" "+self.team+" "+self.country+" "+str(self.podiums)+" "+str(self.points)+" "+str(self.Date)


class Equipos(models.Model):
    name=models.CharField(max_length=50)
    base=models.CharField(max_length=50)
    chief=models.CharField(max_length=50)
    chassis=models.CharField(max_length=50)
    powerunit=models.CharField(max_length=50)
    def __str__(self):
        return self.name+" "+self.base+" "+self.chief+" "+self.chassis+" "+self.powerunit


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
    
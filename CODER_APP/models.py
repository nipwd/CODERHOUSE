from django.db import models

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
    laps=models.IntegerField
    length=models.FloatField(max_length=50)
    record=models.FloatField(max_length=50)
    def __str__(self):
        return self.name+" "+self.country+" "+str(self.laps)+" "+str(self.length)+" "+str(self.record)

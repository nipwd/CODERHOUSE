from django.db import models

# Create your models here.

class Pilotos(models.Model):
    team=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    podiums= models.IntegerField()
    points= models.FloatField()
    Date=models.CharField(max_length=50)
    def __str__(self):
        return self.termino  


class Equipos(models.Model):
    name=models.CharField(max_length=50)
    base=models.CharField(max_length=50)
    chief=models.CharField(max_length=50)
    chassis=models.CharField(max_length=50)
    powerunit=models.CharField(max_length=50)
    world_championships:models.IntegerField()
    def __str__(self):
        return self.termino


class Pistas(models.Model):
    name=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    laps=models.IntegerField
    length=models.FloatField(max_length=50)
    record=models.FloatField(max_length=50)
    def __str__(self):
        return self.termino


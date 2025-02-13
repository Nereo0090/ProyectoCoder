from django.db import models

# Create your models here.
class Torneo (models.Model):

    nombre = models.CharField(max_length=40)

    tipo= models.CharField(max_length=40)

    categoria = models.CharField(max_length=40)

    sede = models.CharField(max_length=40)

    inicio = models.DateField()

    def __str__ (self):

        return f"TORNEO: {self.nombre}"


class Sede (models.Model):

    nombre = models.CharField(max_length=40)

    ubicacion = models.CharField(max_length=40)

    estacionamiento = models.BooleanField ()

    vestuarios = models.BooleanField ()


    def __str__ (self):

        return f"NOMBRE: {self.nombre}"

class Equipo (models.Model):

    nombre = models.CharField(max_length=40)

    localidad = models.CharField(max_length=40)

    torneo = models.CharField(max_length=40)
    
    def __str__ (self):

        return f"EQUIPO: {self.nombre}"



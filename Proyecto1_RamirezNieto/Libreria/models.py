from django.db import models

class Libros(models.Model):
    nombre = models.CharField(max_length=100)
    id = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=100)
    fecha_creacion = models.DateField()
    escritor = models.CharField(max_length=100)

class Revistas(models.Model):
    nombre = models.CharField(max_length=100)
    id = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=100)
    fecha_creacion = models.DateField()
    editorial = models.CharField(max_length=100)

class Audios(models.Model):
    nombre = models.CharField(max_length=100)
    id = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=100)
    fecha_creacion = models.DateField()
    duracion = models.TimeField()




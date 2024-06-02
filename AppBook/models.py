from django.db import models

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=40)
    autor = models.CharField(max_length=60)
    genero= models.CharField(max_length=25)
    año_de_publicacion = models.IntegerField()

class Autores(models.Model):
    nombre = models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    nacionalidad= models.CharField(max_length=25)

class Editoriales(models.Model):
    nombre = models.CharField(max_length=40)
    pais= models.CharField(max_length=40)
    direccion = models.CharField(max_length=50)

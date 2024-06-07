from django.db import models

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=40)
    autor = models.CharField(max_length=60)
    genero= models.CharField(max_length=25)
    año_de_publicacion = models.IntegerField()
    resena= models.TextField(default="Sin reseñas")

    def __str__(self):
        return f"{self.titulo}-{self.autor}-{self.genero}-{self.año_de_publicacion}"


class Autores(models.Model):
    nombre = models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    nacionalidad= models.CharField(max_length=25)
    def __str__(self):
        return f"{self.nombre}-{self.apellido}-{self.nacionalidad}"

class Editoriales(models.Model):
    nombre = models.CharField(max_length=40)
    pais= models.CharField(max_length=40)
    direccion = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.nombre}-{self.pais}-{self.direccion}"
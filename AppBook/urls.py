from django.contrib import admin
from django.urls import path
from AppBook.views import inicio, libros, editoriales, autores

urlpatterns = [
    path('', inicio, name = "Inicio"),
    path('libros/', libros, name = "Libros"),
    path('autores/', autores, name = "Autores"),
    path('editoriales/', editoriales, name = "Editoriales"),
]

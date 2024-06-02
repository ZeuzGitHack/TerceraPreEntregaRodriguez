from django.contrib import admin
from django.urls import path
from AppBook.views import inicio, libros, editoriales, autores

urlpatterns = [
    path('', inicio, name = "Inicio"),
    path('libros/', libros, name = "Libros"),
    path('autor/', autores, name = "Autores"),
    path('editorial/', editoriales, name = "Editoriales"),
]

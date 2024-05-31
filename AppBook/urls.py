from django.contrib import admin
from django.urls import path
from AppBook.views import inicio, libros, editorial, autor

urlpatterns = [
    path('', inicio, name = "Inicio"),
    path('libros/', libros, name = "Libros"),
    path('autor/', autor, name = "Autor"),
    path('editorial/', editorial, name = "Editorial"),
]

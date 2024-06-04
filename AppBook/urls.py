from django.urls import path
from AppBook.views import (
    inicio, 
    libros, 
    editoriales, 
    autores, 
    formularioLibro,
    formularioAutor,
    formularioEditorial,
    )

urlpatterns = [
    path('', inicio, name = "Inicio"),
    path('libros/', libros, name = "Libros"),
    path('autores/', autores, name = "Autores"),
    path('editoriales/', editoriales, name = "Editoriales"),
    path('formulario-libro/', formularioLibro, name = "FormularioLibro"),
    path('formulario-autor/', formularioAutor, name = "FormularioAutor"),
    path('formulario-editorial/', formularioEditorial, name = "FormularioEditorial"),
]

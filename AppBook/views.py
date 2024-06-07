from django.shortcuts import render
from AppBook.models import Libro, Autores, Editoriales
from AppBook.forms import LibroFormulario, AutorFormulario, EditorialFormulario
from django.http import HttpRequest

# Create your views here.
def inicio(req):
    return render(req, "inicio.html", {})

def libros(req):
	lista_libros = Libro.objects.all()
	return render(req, "libros.html", {"lista_libros":lista_libros})

def autores(req):
	lista_autores = Autores.objects.all()
	return render(req, "autores.html", {"lista_autores":lista_autores})

def editoriales(req):
	lista_editoriales = Editoriales.objects.all()
	return render(req, "editoriales.html", {"lista_editoriales":lista_editoriales})

def formularioLibro(req):
	if req.method == "POST":
		form_libro = LibroFormulario(req.POST)
		print(form_libro)
		if form_libro.is_valid:
			informacion = form_libro.cleaned_data
			libro = Libro(titulo=informacion["titulo"], autor=informacion["autor"], genero=informacion["genero"], año_de_publicacion=informacion["año_de_publicacion"], reseña=informacion["reseña"])
			libro.save()
			return render(req, "inicio.html",{"mensaje": "Se guardo nuevo Libro"})
		else:
			return render(req, "inicio.html", {"mensaje": "Datos incorrectos"})
			
	else:
		form_libro = LibroFormulario()
	return render(req, "formulariosLibro.html", {"form_libro": form_libro})

def formularioAutor(req):
	if req.method == "POST":
		form_autor = AutorFormulario(req.POST)
		print(form_autor)
		if form_autor.is_valid:
			informacion = form_autor.cleaned_data
			autor = Autores(nombre=informacion["nombre"], apellido=informacion["apellido"], nacionalidad=informacion["nacionalidad"])
			autor.save()
			return render(req, "inicio.html",{"mensaje":"Se guardo nuevo Autor"})
		else:
			return render(req, "inicio.html", {"mensaje":"Datos incorrectos"})
	else:
		form_autor = AutorFormulario()
	return render(req, "formulariosAutor.html", {"form_autor": form_autor})

def formularioEditorial(req):
	if req.method == "POST":
		form_editorial = EditorialFormulario(req.POST)
		print(form_editorial)
		if form_editorial.is_valid:
			informacion = form_editorial.cleaned_data
			editorial = Editoriales(nombre=informacion["nombre"], pais=informacion["pais"], direccion=informacion["direccion"])
			editorial.save()
			return render(req, "inicio.html",{"mensaje":"Se guardo nueva Editorial"})
		else:
			return render(req, "inicio.html", {"mensaje":"Datos incorrectos"})
	else:
		form_editorial = EditorialFormulario()
	return render(req, "formulariosEditorial.html", {"form_editorial": form_editorial})

def busquedaLibro(req):
	return render(req, "resultadoBusqueda.html")

def buscar(req):
	try:
		if req.GET["libro"]:
			libro = req.GET["libro"]
			libros = Libro.objects.get(titulo=libro)
			return render(req, "resultadoBusqueda.html", {"libro":libros})
		else:
			return render(req, "resultadoBusqueda.html", {"mensaje":"Ingrese un Titulo"})
	except:
		return render(req, "resultadoBusqueda.html", {"mensaje":"Libro no encontrado"})


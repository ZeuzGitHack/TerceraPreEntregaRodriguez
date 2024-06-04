from django.shortcuts import render
from AppBook.models import Libro, Autores, Editoriales
from AppBook.forms import LibroFormulario, AutorFormulario, EditorialFormulario

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
		form_libro = LibroFormulario(req.POST) # Aqui me llega la informacion del html
		print(form_libro)
		if form_libro.is_valid:
			informacion = form_libro.cleaned_data
			libro = Libro(titulo=informacion["titulo"], autor=informacion["autor"], genero=informacion["genero"], año_de_publicacion=informacion["año_de_publicacion"])
			libro.save()
			return render(req, "inicio.html")
	else:
		form_libro = LibroFormulario()
	return render(req, "formulariosLibro.html", {"form_libro": form_libro})

def formularioAutor(req):
	if req.method == "POST":
		form_autor = AutorFormulario(req.POST) # Aqui me llega la informacion del html
		print(form_autor)
		if form_autor.is_valid:
			informacion = form_autor.cleaned_data
			autor = Autores(nombre=informacion["nombre"], apellido=informacion["apellido"], nacionalidad=informacion["nacionalidad"])
			autor.save()
			return render(req, "inicio.html")
	else:
		form_autor = AutorFormulario()
	return render(req, "formulariosAutor.html", {"form_autor": form_autor})

def formularioEditorial(req):
	if req.method == "POST":
		form_editorial = EditorialFormulario(req.POST) # Aqui me llega la informacion del html
		print(form_editorial)
		if form_editorial.is_valid:
			informacion = form_editorial.cleaned_data
			editorial = Editoriales(nombre=informacion["nombre"], pais=informacion["pais"], direccion=informacion["direccion"])
			editorial.save()
			return render(req, "inicio.html")
	else:
		form_editorial = EditorialFormulario()
	return render(req, "formulariosEditorial.html", {"form_editorial": form_editorial})

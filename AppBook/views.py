from django.shortcuts import render
from AppBook.models import Libro
from AppBook.forms import LibroFormulario

# Create your views here.
def inicio(req):
    return render(req, "inicio.html", {})

def libros(req):
    return render(req, "libros.html", {})

def autores(req):
    return render(req, "autores.html", {})

def editoriales(req):
    return render(req, "editoriales.html", {})

# def formularioLibro(req):
# 	if req.method == 'POST':
# 		libro = Libro(req.post['titulo'],req.post['autor'], req.post['genero'], req.post['año_de_publicacion'])
# 		libro.save()
# 		return render(req, "AppBook/inicio.html", {})
# 	return render(req,"AppBook/formularioLibro.html", {})

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

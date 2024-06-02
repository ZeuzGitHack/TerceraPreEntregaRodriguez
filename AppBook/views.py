from django.shortcuts import render

# Create your views here.
def inicio(req):
    return render(req, "inicio.html", {})

def libros(req):
    return render(req, "libros.html", {})

def autores(req):
    return render(req, "autores.html", {})

def editoriales(req):
    return render(req, "editoriales.html", {})
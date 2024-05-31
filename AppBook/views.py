from django.shortcuts import render

# Create your views here.
def inicio(req):
    return render(req, "inicio.html", {})

def libros(req):
    return render(req, "libros.html", {})

def autor(req):
    return render(req, "autor.html", {})

def editorial(req):
    return render(req, "editorial.html", {})
from django import forms
from .models import Libro


class LibroFormulario(forms.Form):
	titulo= forms.CharField()
	autor= forms.CharField()
	genero= forms.CharField()
	año_de_publicacion = forms.IntegerField()
	resena= forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 30}))
	class Meta:
		model = Libro
		fields = ['campo_texto']

class AutorFormulario(forms.Form):
	nombre= forms.CharField()
	apellido= forms.CharField()
	nacionalidad= forms.CharField()


class EditorialFormulario(forms.Form):
	nombre= forms.CharField()
	pais= forms.CharField()
	direccion= forms.CharField()


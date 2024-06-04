from django import forms


class LibroFormulario(forms.Form):
	titulo= forms.CharField()
	autor= forms.CharField()
	genero= forms.CharField()
	año_de_publicacion = forms.IntegerField()

class AutorFormulario(forms.Form):
	nombre= forms.CharField()
	apellido= forms.CharField()
	nacionalidad= forms.CharField()


class EditorialFormulario(forms.Form):
	nombre= forms.CharField()
	pais= forms.CharField()
	direccion= forms.CharField()


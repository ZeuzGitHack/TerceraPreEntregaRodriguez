from django import forms


class LibroFormulario(forms.Form):
	titulo= forms.CharField()
	autor= forms.CharField()
	genero= forms.CharField()
	año_de_publicacion = forms.IntegerField()

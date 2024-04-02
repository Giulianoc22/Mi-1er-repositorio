from django import forms

class Curso_formulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    camada = forms.IntegerField()

class Alumno_formulario(forms.Form):
    nombre = forms.CharField(max_length=15)
    apellido = forms.CharField(max_length=15)

class Profesor_formulario(forms.Form):
    nombre = forms.CharField(max_length=15)
    apellido = forms.CharField(max_length=15)
    email = forms.EmailField()
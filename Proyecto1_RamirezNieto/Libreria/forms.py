from django import forms

class LibrosForm(forms.Form):
    nombre = forms.CharField()
    id = forms.IntegerField()
    tipo = forms.CharField()
    fecha_creacion = forms.DateField()
    escritor = forms.CharField()

class RevistasForm(forms.Form):
    nombre = forms.CharField()
    id = forms.IntegerField()
    tipo = forms.CharField()
    fecha_creacion = forms.DateField()
    editorial = forms.CharField()

class AudiosForm(forms.Form):
    nombre = forms.CharField()
    id = forms.IntegerField()
    tipo = forms.CharField()
    fecha_creacion = forms.DateField()
    duracion = forms.TimeField()

class SearchForm(forms.Form):
    nombre  = forms.CharField()


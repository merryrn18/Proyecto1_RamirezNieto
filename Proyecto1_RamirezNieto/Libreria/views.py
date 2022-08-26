from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.template import Context, Template,loader
from django.http import HttpRequest,HttpResponse
from Libreria.forms import LibrosForm,RevistasForm,AudiosForm,SearchForm
from Libreria.models import Libros,Revistas,Audios

def inicio(request):
    return render(request,'index.html')

def libros(request):

    libs = Libros.objects.all()

    contexto = {"libros":libs}
    return render(request,'libros.html',contexto)

def addLibros(request):
    if request.method == "POST":
        formulario = LibrosForm(request.POST)

        if formulario.is_valid():
            info = formulario.cleaned_data
            libro = Libros(nombre = info['nombre'],id = info['id'],tipo = info['tipo'],fecha_creacion = info['fecha_creacion'],escritor = info['escritor'])
            libro.save()
            return redirect("LibreriaLibros")
    else:
        formulario  = LibrosForm()

    return render(request,"add.html",{"formulario":formulario})

def searchLibros(request):
    formulario  = SearchForm()
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre = info["nombre"]
            libros = Libros.objects.filter(nombre__icontains = nombre)
            return render(request,'searchLibros.html',{"formulario":formulario,"libros":libros})
    else:
        return render(request,'searchLibros.html',{"formulario":formulario})

def revistas(request):

    revs = Revistas.objects.all()

    contexto = {"revistas":revs}
    return render(request,'revistas.html',contexto)
    
def addRevistas(request):
    if request.method == "POST":
        formulario = RevistasForm(request.POST)

        if formulario.is_valid():
            info = formulario.cleaned_data
            revista = Revistas(nombre = info['nombre'],id = info['id'],tipo = info['tipo'],fecha_creacion = info['fecha_creacion'],editorial = info['editorial'])
            revista.save()
            return redirect("LibreriaRevistas")
    else:
        formulario  = RevistasForm()

    return render(request,"add.html",{"formulario":formulario})

def searchRevistas(request):
    formulario  = SearchForm()
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre = info["nombre"]
            revistas = Revistas.objects.filter(nombre__icontains = nombre)
            return render(request,'searchRevistas.html',{"formulario":formulario,"revistas":revistas})
    else:
        return render(request,'searchRevistas.html',{"formulario":formulario})

def audios(request):

    auds = Audios.objects.all()

    contexto = {"audios":auds}
    return render(request,'audios.html',contexto)
    
def addAudios(request):
    if request.method == "POST":
        formulario = AudiosForm(request.POST)

        if formulario.is_valid():
            info = formulario.cleaned_data
            audio = Libros(nombre = info['nombre'],id = info['id'],tipo = info['tipo'],fecha_creacion = info['fecha_creacion'],duracion = info['duracion'])
            audio.save()
            return redirect("LibreriaAudios")
    else:
        formulario  = RevistasForm()

    return render(request,"Libreria/add.html",{"formulario":formulario})

def searchAudios(request):
    formulario  = SearchForm()
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre = info["nombre"]
            audios = Audios.objects.filter(nombre__icontains = nombre)
            return render(request,'Libreria/searchAudios.html',{"formulario":formulario,"audios":audios})
    else:
        return render(request,'Libreria/searchAudios.html',{"formulario":formulario})
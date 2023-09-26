from django.shortcuts import render, HttpResponse

# Create your views here.

def homeCatalogos(request):
    return render(request, 'home.html')

def aulasCreate(request):
    return HttpResponse('<h1>Creando nueva Aula</h1>')

def aulasList(request):
    return HttpResponse('<h1>Lista de Aulas</h1>')

def aulasDelete(request):
    return HttpResponse('<h1>Eliminando una Aula</h1>')

def aulasUpdate(request):
    return HttpResponse('<h1>Modificando una Aula</h1>')

from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1>Bienvenido a mi Sistema</h1>\
                        <h3>Estás en el home de mi proyecto</h3>')

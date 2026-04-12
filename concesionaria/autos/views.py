from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def autos(request):
    return HttpResponse("hola pagina de autos XD")

def inicio(request):
    return HttpResponse("hola pagina de inicio XD")
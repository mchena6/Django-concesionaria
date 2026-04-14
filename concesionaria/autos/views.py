from django.shortcuts import render
from autos.models import Auto
# Create your views here.

def autos(request):
    autos = Auto.objects.all()
    return render(request, "autos/autos.html", {"autos": autos})

def inicio(request):
    return render(request, "autos/inicio.html")
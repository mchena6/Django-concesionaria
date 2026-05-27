from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth.decorators import login_required

from django.contrib.auth import login
from .forms import UsuarioPersonalizadoForm

# Create your views here.

def registrarse(request):
    if request.method == "POST":
        form = UsuarioPersonalizadoForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("autos")
    else:
        form = UsuarioPersonalizadoForm()
    return render(request, "registration/register.html", {"form": form})
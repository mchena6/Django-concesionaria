from django.shortcuts import render, redirect, get_object_or_404
from autos.models import Auto, Vendedor
from .forms import AutoForm, VendedorForm

# Create your views here.


def autos(request):
    autos = Auto.objects.all().order_by("-id").filter(activo=True)
    return render(request, "autos/autos.html", {"autos": autos})


def inicio(request):
    return render(request, "autos/inicio.html")


def crear_auto(request):
    if request.method == "POST":
        form = AutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("autos")
    else:
        form = AutoForm()
    return render(request, "autos/crear_auto.html", {"form": form})


def editar_auto(request, id):
    auto = get_object_or_404(Auto, id=id)

    if request.method == "POST":
        form = AutoForm(request.POST, instance=auto)
        if form.is_valid():
            form.save()
            return redirect("autos")
    else:
        form = AutoForm(instance=auto)

    return render(request, "autos/editar_auto.html", {"form": form})


def eliminar_auto(request, id):
    auto = get_object_or_404(Auto, id=id)
    if request.method == "POST":
        auto.activo = False
        auto.save()

        return redirect("autos")
    return render(request, "autos/eliminar_auto.html", {"auto": auto})


def crear_vendedor(request):
    if request.method == "POST":
        form = VendedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("autos")
    else:
        form = VendedorForm()
        return render(request, "autos/crear_vendedor.html", {"form": form})


def editar_vendedor(request, id):
    vendedor = get_object_or_404(Vendedor, id=id)

    if request.method == "POST":
        form = VendedorForm(request.POST, instance = vendedor)
        if form.is_valid():
            form.save()
            return redirect("autos")
        
    else: 
        form = VendedorForm(instance = vendedor)

    return render(request, "autos/editar_vendedor.html", {"form": form})


def eliminar_vendedor(request, id):
    vendedor = get_object_or_404(Vendedor, id=id)

    if request.method == "POST":
        vendedor.activo = False
        vendedor.save()

        return redirect("autos")
    
    return render(request, "autos/eliminar_vendedor.html", {"vendedor": vendedor})
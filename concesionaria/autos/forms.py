from django import forms

from .models import Auto, Vendedor

class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = [
            "marca",
            "modelo",
            "anio",
            "precio",
            "color",
            "vendedor",
        ]

class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = [
            "nombre",
            "email",
            "telefono",
        ]
        
from django import forms

from .models import Auto

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
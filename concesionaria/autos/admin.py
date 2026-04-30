from django.contrib import admin
from .models import Auto, Vendedor

# Register your models here.

@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ("marca", "modelo", "anio", "precio", "color", "activo")
    search_fields = ("marca",)

admin.site.register(Vendedor)
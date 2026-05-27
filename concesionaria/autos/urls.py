from django.urls import path
from . import views

urlpatterns= [
        path("", views.inicio, name="inicio"),
        path("autos/", views.autos, name="autos"),
        path("crear", views.crear_auto, name="crear_auto"),
        path("editar/<int:id>", views.editar_auto, name="editar_auto"),
        path("eliminar/<int:id>",views.eliminar_auto, name="eliminar_auto"),
        path("crear_vendedor", views.crear_vendedor, name="crear_vendedor"),
        path("registrarse/", views.registrarse, name="registrarse"),
]
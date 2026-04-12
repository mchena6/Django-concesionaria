from django.urls import path
from . import views

urlpatterns= [
        path("", views.inicio, name="inicio"),
        path("autos/", views.autos, name="autos"),
]
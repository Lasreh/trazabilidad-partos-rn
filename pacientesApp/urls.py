from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pacientes, name='lista_pacientes'),
    path("crear/", views.crear_paciente, name="crear_paciente"),
    path("hospitalizaciones/", views.lista_hospitalizaciones, name="lista_hospitalizaciones"),
]
from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_parto, name='crear_parto'),

    path('<int:pk>/editar/', views.editar_parto, name='editar_parto'),

    # Anestesia
    path('<int:pk>/anestesia/', views.editar_anestesia, name='editar_anestesia'),
    path('<int:pk>/anestesia/crear/', views.crear_anestesia, name='crear_anestesia'),

    # Finalizar proceso
    path('<int:pk>/finalizar/', views.finalizar_parto, name='finalizar_parto'),

    # Listar partos
    path('lista/', views.lista_partos, name='lista_partos'),
]

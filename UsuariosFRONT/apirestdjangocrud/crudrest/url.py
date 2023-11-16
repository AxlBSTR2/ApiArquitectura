from django.urls import path
from .import views

urlpatterns = [
    path('', views.ServiciosLista, name="productos"),
    path('detalle/<str:pk>', views.ServiciosDetalle, name="detalle"),
    path('crear', views.ServiciosCrear, name="crear"),
    path('actualizar/<str:pk>/', views.ServiciosActualizar, name="actualizar"),
    path('eliminar/<str:pk>/', views.ServiciosEliminar, name="eliminar"),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.saludar, name='base'),
    path('cliente/', views.cliente_form_view, name='cliente_form'),
    path('articulo/', views.articulo_form_view, name='articulo_form'),
    path('venta/', views.venta_form_view, name='venta_form'),
]


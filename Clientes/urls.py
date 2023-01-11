from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('', views.saludar, name='base'),
    path('cliente/', views.cliente_form_view, name='cliente_form'),
    path('articulo/', views.articulo_form_view, name='articulo_form'),
    path('venta/', views.venta_form_view, name='venta_form'),
    path('login/', LoginView.as_view(template_name = "login.html"), name='login'),
    path('logout/', LogoutView.as_view(template_name = "logout.html"), name='logout'),
    path('register/', views.register_view, name='register')
]


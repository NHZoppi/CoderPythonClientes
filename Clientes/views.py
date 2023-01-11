from django.shortcuts import render, redirect
from .forms import ClienteForm, VentaForm, ArticuloForm, RegisterForm
from .models import Cliente, Venta, Articulos
from datetime import datetime
from django.contrib.auth import login, authenticate
from django.contrib import messages

def cliente_form_view(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            return render(request, "cliente_form.html", {"form":form, "cliente":cliente})
    else:
        form = ClienteForm()
    return render(request, 'cliente_form.html', {'form': form})

def articulo_form_view(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ArticuloForm()
    return render(request, 'articulo_form.html', {'form': form})



def venta_form_view(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = Venta()
            fecha = '31/12/2022'  # Cadena de texto con formato "día/mes/año"
            fecha = datetime.strptime(fecha, "%d/%m/%Y").date()
            venta.fecha = fecha
            form.save()
    else:
        form = VentaForm()
    return render(request, 'venta_form.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # Procesa los datos del formulario
            username = form.cleaned_data.get('username')
            messages.success(request, f"Usuario {username} creado")
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            return redirect ("base")
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})



def saludar(request):
    return render(
        request,
        "base.html"
    )
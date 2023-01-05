from django.shortcuts import render
from .forms import ClienteForm, VentaForm, ArticuloForm
from .models import Cliente, Venta, Articulos
from datetime import datetime

def cliente_form_view(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
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

def saludar(request):
    return render(
        request,
        "base.html"
    )
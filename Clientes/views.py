from django.shortcuts import render

from .forms import ClienteForm, VentaForm, ArticuloForm

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
            form.save()
    else:
        form = VentaForm()
    return render(request, 'venta_form.html', {'form': form})

def saludar(request):
    return render(
        request=request,
        template_name='Clientes/base.html',
    )
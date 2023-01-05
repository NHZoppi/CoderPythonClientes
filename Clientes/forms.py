from django import forms
from django import forms
from Clientes.models import Cliente, Articulos, Venta


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulos
        fields = "__all__"

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = "__all__"
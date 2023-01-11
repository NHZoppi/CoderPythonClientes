from django import forms
from django import forms
from Clientes.models import Cliente, Articulos, Venta
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cliente'].label_from_instance = lambda obj: obj.nombre
        self.fields['articulo'].label_from_instance = lambda obj: obj.nombre

class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'class':'form-control'}))
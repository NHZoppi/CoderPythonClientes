from django.contrib import admin
from Clientes.models import Venta, Articulos, Cliente
# Register your models here.

admin.site.register(Venta)
admin.site.register(Articulos)
admin.site.register(Cliente)
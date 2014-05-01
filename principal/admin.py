from django.contrib import admin
from empleados.models import Empleado
from clientes.models import Cliente
from producto.models import Producto,PromocionProducto
from proveedores.models import Proveedor
from factura.models import Factura,Impuesto,Productos,ProductosFactura,NotaCredito,ProductosNota,NotaCreditoProductosNota

admin.site.register(Empleado)
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(PromocionProducto)
admin.site.register(Proveedor)
admin.site.register(Factura)
admin.site.register(ProductosFactura)
admin.site.register(Impuesto)
admin.site.register(Productos)
admin.site.register(NotaCredito)
admin.site.register(ProductosNota)
admin.site.register(NotaCreditoProductosNota)

from django.db import models
from django.contrib import admin



# Register your models here.

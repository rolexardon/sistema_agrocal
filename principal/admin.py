from django.contrib import admin
from empleados.models import Empleado
from clientes.models import Cliente
from producto.models import Producto,PromocionProducto
from proveedores.models import Proveedor
from factura.models import Factura,Impuesto,Productos,ProductosFactura,NotaCredito,ProductosNota,NotaCreditoProductosNota
from inventario.models import compra, compra_producto, bodega, producto_transferencia, producto_bodega

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

class CompraProductInline(admin.StackedInline):
    model = compra_producto

class CompraAdmin(admin.ModelAdmin):
	list_display = ['orden_compra', 'proveedor','fecha']
	list_select_related = True
	inlines = [CompraProductInline]
    #filter_horizontal = ('producto',)
    
class transferenciaAdmin(admin.ModelAdmin):
    list_display = ('producto','cantidad','bodega_origen','bodega_destino','fecha_creacion','usuario_creador','total_origen','total_destino')
    
    def get_form(self, request, obj=None, **kwargs):
		if obj == None:
			self.exclude = ("total_origen",'total_destino', )
		form = super(transferenciaAdmin, self).get_form(request, obj, **kwargs)
		return form
		
class BodegaProductInline(admin.StackedInline):
    model = producto_bodega

class BodegaAdmin(admin.ModelAdmin):
	#list_display = ['orden_compra', 'proveedor','fecha']
	list_select_related = True
	inlines = [BodegaProductInline]
	#filter_horizontal = ('producto',)

	def get_form(self, request, obj=None, **kwargs):
		if obj == None:
			self.exclude = ("producto",'bodega', )
		form = super(BodegaAdmin, self).get_form(request, obj, **kwargs)
		return form
    
admin.site.register(compra,CompraAdmin)
admin.site.register(bodega, BodegaAdmin)
admin.site.register(producto_transferencia,transferenciaAdmin)

    
from django.db import models
from django.contrib import admin



# Register your models here.

from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from empleados.models import Empleado
from clientes.models import Cliente
from producto.models import Producto,PromocionProducto
from proveedores.models import Proveedor
from factura.models import Factura,Impuesto,Productos,ProductosFactura,NotaCredito,ProductosNota,NotaCreditoProductosNota
from inventario.models import compra, compra_producto, bodega, producto_transferencia, producto_bodega

admin.site.unregister(User)
admin.site.register(PromocionProducto)
admin.site.register(Proveedor)
admin.site.register(Factura)
#admin.site.register(ProductosFactura)
admin.site.register(Impuesto)
admin.site.register(Productos)
admin.site.register(NotaCredito)
admin.site.register(ProductosNota)
admin.site.register(NotaCreditoProductosNota)

class EmpleadoInline(admin.StackedInline):
    model = Empleado
    max_num = 1
    

class EmpleadoAdmin(admin.ModelAdmin):
	inlines = [EmpleadoInline]
	
	def save_model(self, request, obj, form, change):
		obj.set_password(obj.password)
		obj.save()
	"""
	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == 'usuario_creador':
			kwargs['initial'] = request.user.id
		return super(EmpleadoInline, self).formfield_for_foreignkey(db_field, request, **kwargs)"""
		
class ClienteAdmin(admin.ModelAdmin):
	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == 'usuario_creador':
			kwargs['initial'] = request.user.id
		return super(ClienteAdmin, self).formfield_for_foreignkey(
			db_field, request, **kwargs
		)	
		
class ProductoAdmin(admin.ModelAdmin):
	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == 'usuario_creador':
			kwargs['initial'] = request.user.id
		return super(ProductoAdmin, self).formfield_for_foreignkey(
			db_field, request, **kwargs
		)

class CompraProductInline(admin.TabularInline):
    model = compra_producto
    extra = 1

class CompraAdmin(admin.ModelAdmin):
	#readonly_fields = ['numero_compra','total_compra','subtotal_compra']
	readonly_fields = ['subtotal_compra','total_compra']
	list_display = ['orden_compra']
	
	list_select_related = True
	inlines = [CompraProductInline]
	
	def numero_compra(self, obj):
		if obj.orden_compra is None:
			a = compra.objects.all().order_by('-orden_compra')[:1]
			if a:
				return a[0].a + 1
			else:
				return 1
		else:
			return obj.orden_compra
			
	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == 'usuario_creador':
			kwargs['initial'] = request.user.id
		return super(CompraAdmin, self).formfield_for_foreignkey(
			db_field, request, **kwargs
		)

class transferenciaAdmin(admin.ModelAdmin):
    list_display = ('producto','cantidad','bodega_origen','bodega_destino','fecha_creacion','usuario_creador','total_origen','total_destino')

    def get_form(self, request, obj=None, **kwargs):
		if obj == None:
			self.exclude = ("total_origen",'total_destino', )
		form = super(transferenciaAdmin, self).get_form(request, obj, **kwargs)
		return form
		
class BodegaProductInline(admin.TabularInline):
    model = producto_bodega
    exclude = ('transaccion',)
    extra = 0
		
class BodegaAdmin(admin.ModelAdmin):
	#list_display = ('producto', 'cantidad')
	inlines = [BodegaProductInline]
	"""
	def get_form(self, request, obj=None, **kwargs):
		print obj
		if obj == None:
			self.inline_instances = []
		form = super(BodegaAdmin, self).get_form(request, obj, **kwargs)
		return form

	def get_readonly_fields(self, request, obj=None):
		print obj
		if obj == None:
			self.inline_instances = []
			print '01', self
			return ()
		else:
			print '02', self
			return ()
	"""	
        
        
admin.site.register(compra,CompraAdmin)
admin.site.register(bodega, BodegaAdmin)
admin.site.register(Cliente, ClienteAdmin)
#admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(User, EmpleadoAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(producto_transferencia,transferenciaAdmin)


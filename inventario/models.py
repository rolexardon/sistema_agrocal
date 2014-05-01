# -*- coding: utf8 -*-
from django.db import models
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.contrib.auth.models import User
from empleados.models import Empleado
from proveedores.models import Proveedor
from producto.models import Producto


	
class bodega(models.Model):
	codigo = models.CharField(max_length='20',unique = True,blank=False,null=False)
	nombre = models.CharField(max_length='50',blank = False,null = False)
	descripcion = models.TextField(max_length='250',blank = False,null = False)
	encargado = models.ForeignKey(Empleado,unique = True)
	
	def __unicode__(self):
		return '%s | %s %s' % (self.nombre, self.encargado.p_nombre, self.encargado.p_apellido)
        
	def clean(self):
        # NO guardar empleado que no sea vendedor
		if self.encargado.tipo != 'Vendedor':
			raise ValidationError('Asegúrese que el empleado sea un vendedor.')
 			
	def delete(self, *args, **kwargs):
        # Evitar que se borre la bodega principal
		if self.pk == 1 :
			raise ValidationError("NO se puede eliminar la bodega principal")
			
def get_bodega_principal():
	b = bodega.objects.filter(pk=1)
	if b:
		return b[0]
	else:
		return None
	
class producto_bodega(models.Model):
	producto = models.ForeignKey(Producto)
	bodega = models.ForeignKey(bodega, default = get_bodega_principal)
	cantidad = models.IntegerField(blank = False,null = False)
	transaccion = models.IntegerField(default = 2) # para saber si esta añadiendo o modificando la cantidad, 0 es restar, 1 sumar, 2 se reemplaza
	
	class Meta:
		unique_together = ("producto","bodega")
	
	def save(self, *args, **kwargs):
        #Si se intenta agregar mas cantidad de un producto
		pb = producto_bodega.objects.filter(producto = self.producto, bodega = self.bodega)
		#incluir validacion de transaccion
		if pb:
			if self.transaccion == 1:
				pb.update(cantidad = pb[0].cantidad + self.cantidad,transaccion = 2)
			if self.transaccion == 0:
				pb.update(cantidad = pb[0].cantidad - self.cantidad,transaccion = 2)
			if self.transaccion == 2:
				pb.update(cantidad = self.cantidad)
		else:
			super(producto_bodega, self).save(*args, **kwargs)

		
class compra(models.Model):
	orden_compra = models.AutoField(primary_key=True)
	proveedor = models.ForeignKey(Proveedor,related_name='compra_proveedor')
	fecha = models.DateField(null = False)
	#total_compra
	
	fecha_creacion = models.DateTimeField(auto_now_add = True,null = False)
	usuario_creador = models.ForeignKey(User)
	
class compra_producto(models.Model):
	compra = models.ForeignKey(compra)
	producto = models.ForeignKey(Producto)
	cantidad = models.IntegerField(blank = False,null = False)
	costo = models.DecimalField(max_digits=12, decimal_places=2,blank = False,null = False)
	
	class Meta:
		unique_together = ("compra", "producto")
       
	def save(self, *args, **kwargs):
        #Alimentar inventario de bodega principal
		producto = self.producto
		cantidad = self.cantidad
		producto_bodega.objects.create(producto = producto,cantidad = cantidad,transaccion = 1)

		super(compra_producto, self).save(*args, **kwargs)

	
class producto_transferencia(models.Model):
	producto = models.ForeignKey(Producto)
	bodega_origen = models.ForeignKey(bodega, related_name='bodega')
	bodega_destino = models.ForeignKey('bodega', related_name='bodega_destino')
	cantidad = models.IntegerField(blank = False,null = False)
	total_origen = models.IntegerField(blank = False,null = False)
	total_destino = models.IntegerField(blank = False,null = False)
	
	fecha_creacion = models.DateTimeField(auto_now_add = True,null = False)
	usuario_creador = models.ForeignKey(User)
    
	def clean(self):
        #Validar que se pueda realizar transaccion
		bodega_origen = self.bodega_origen
		producto = self.producto
		cantidad = self.cantidad
		
		cantidad_pb = producto_bodega.objects.filter(bodega = bodega_origen,producto=producto)[0].cantidad
		 
		if cantidad_pb < cantidad:
			raise ValidationError('NO existen suficientes elementos para realizar transferencia.')
			
	def save(self, *args, **kwargs):
		#Guardar elementos y actualizar valores de estado
		producto = self.producto
		cantidad = self.cantidad
		bodega_origen = self.bodega_origen
		bodega_destino = self.bodega_destino

		pb_origen = producto_bodega.objects.filter(bodega = bodega_origen,producto=producto)
		pb_destino = producto_bodega.objects.filter(bodega = bodega_destino,producto=producto)
		
		pb_origen.update(cantidad = pb_origen[0].cantidad - self.cantidad)
		if pb_destino:
			pb_destino.update(cantidad = pb_destino[0].cantidad + self.cantidad)
			self.total_destino = pb_destino[0].cantidad
		else:
			producto_bodega.objects.create(producto = producto,bodega = bodega_destino, cantidad = cantidad, transaccion = 1)
			self.total_destino = cantidad
		
		self.total_origen = pb_origen[0].cantidad
		
		
		super(producto_transferencia, self).save(*args, **kwargs)
		
		
	

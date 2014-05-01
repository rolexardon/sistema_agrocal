# -*- coding: utf8 -*-
from django.db import models
from django.contrib.auth.models import User
from empleados.models import Empleado
from proveedores.models import Proveedor
from django.db.models import ImageField

class Producto(models.Model):
    ESTADO=(
        ('SI','SI'),
        ('NO','NO'),
    )

    imagen= models.ImageField(upload_to="imagen_productos/")
    codigo=models.CharField(max_length='125',verbose_name=u'Código :',unique=True)
    nombre= models.CharField(max_length='125', verbose_name=u'Nombre Producto:')
    precio_costo=models.DecimalField(max_digits=10,decimal_places=2,verbose_name=u'Precio Costo')
<<<<<<< HEAD
    precio_preferencial=models.DecimalField(max_digits=10,decimal_places=2,verbose_name=u'Precio Clientes Preferenciales')
    precio_venta_min=models.DecimalField(max_digits=10,decimal_places=2,verbose_name=u'Precio Venta Minimo')
    precio_venta_med=models.DecimalField(max_digits=10,decimal_places=2,verbose_name=u'Precio Venta Medio')
    precio_venta_max=models.DecimalField(max_digits=10,decimal_places=2,verbose_name=u'Precio Venta Maximo')
    cantidad = models.IntegerField(verbose_name=u'Cantidad:')
    descripcion=models.TextField(max_length='250', verbose_name=u'Descripción Producto:')
    proveedor=models.ForeignKey(Proveedor)
=======
    precio_venta_min=models.DecimalField(max_digits=10,decimal_places=2,verbose_name=u'Precio Venta Minimo')
    precio_venta_med=models.DecimalField(max_digits=10,decimal_places=2,verbose_name=u'Precio Venta Medio')
    precio_venta_max=models.DecimalField(max_digits=10,decimal_places=2,verbose_name=u'Precio Venta Maximo')
    #cantidad = models.IntegerField(verbose_name=u'Cantidad:')
    descripcion=models.TextField(max_length='250', verbose_name=u'Descripción Producto:')
    #proveedor=models.ForeignKey(Proveedor)
>>>>>>> 7c6f7ebb9828b38cdb02b715888e268a54ec46f6
    habilitado = models.CharField(max_length='2', verbose_name=u'Habilitado :', choices = ESTADO)
    usuario_creador = models.ForeignKey(User)
    fecha_creacion = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s - %s - %s' % (self.codigo, self.nombre,self.precio_venta_max)

class PromocionProducto(models.Model):
    ESTADO=(
        ('SI','SI'),
        ('NO','NO'),
    )
    id_producto= models.ForeignKey(Producto)
    nombre_promocion=models.CharField(max_length='125', verbose_name=u'Nombre Promoción :')
    porcentaje_descuento=models.DecimalField(max_digits=10,decimal_places=2,verbose_name=u'Descuento %')
    comentarios=models.TextField(max_length='250', verbose_name=u'Comentarios:')
    habilitado = models.CharField(max_length='2', verbose_name=u'Habilitado :', choices = ESTADO)

    def __unicode__(self):
        return '%s - %s ' % (self.id_producto,self.nombre_promocion)

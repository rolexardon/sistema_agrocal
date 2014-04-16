# -*- coding: utf8 -*-
from django.db import models
from django.contrib.auth.models import User
from empleados.models import Empleado
from producto.models import PromocionProducto
from django.db.models import ImageField

class Impuesto(models.Model):
    nombre=models.CharField(max_length='50',verbose_name=u'Nombre :',unique=True)
    impuesto=models.DecimalField(max_digits=10,decimal_places=2,verbose_name=u'impuesto')
    def __unicode__(self):
        return '%s - %s' % (self.nombre, self.impuesto)

class Productos(models.Model):
    nombreProducto= models.CharField(max_length='125', verbose_name=u'Nombre Producto:')
    unidades = models.IntegerField(verbose_name=u'Unidades:')
    precio=models.DecimalField(max_digits=10,decimal_places=2,verbose_name=u'Precio Unitario')
    descuento=models.DecimalField(max_digits=10,decimal_places=2,verbose_name=u'Descuento')
    fecha = models.DateField(auto_now=False)
    total=models.DecimalField(max_digits=10,decimal_places=2,verbose_name=u'Total')
    def __unicode__(self):
        return '%s - %s -%s - %s' % (self.nombreProducto, self.unidades,self.precio,self.total)

class Factura(models.Model):
    VENTA=(
        ('CREDITO','CREDITO'),
        ('CONTADO','CONTADO'),
    )
    numero=models.CharField(verbose_name=u'Número :',unique=True,max_length='125')
    nombre= models.CharField(max_length='125', verbose_name=u'Nombre Cliente:')
    vendedor=models.CharField(max_length='250', verbose_name=u'Vendedor:')
    tipo = models.CharField(max_length='2', verbose_name=u'Tipo de Venta :', choices = VENTA)
    subtotal=models.DecimalField(max_digits=10,decimal_places=2,verbose_name=u'SubTotal')
    #impuesto=models.ForeignKey(Impuesto)
    impuestoaplicado=models.DecimalField(max_digits=10,decimal_places=2,verbose_name=u'Impuesto Aplicado')
    descuentoaplicado=models.DecimalField(max_digits=10,decimal_places=2,verbose_name=u'Descuento Aplicado')
    total=models.DecimalField(max_digits=10,decimal_places=2,verbose_name=u'Total')
    comentario=models.TextField(max_length='250', verbose_name=u'Comentario:')
    usuario_creador = models.ForeignKey(User,null=True,blank=True)
    fecha_creacion = models.DateField(auto_now=False)
    def __unicode__(self):
        return '%s - %s - %s' % (self.numero, self.nombre,self.total)

class ProductosFactura(models.Model):
    id_factura = models.ForeignKey(Factura)
    id_producto = models.ForeignKey(Productos)
    def __unicode__(self):
        return u'%s %s' % (self.id_factura, self.id_producto)


class NotaCredito(models.Model):
    numero=models.CharField(max_length='125',verbose_name=u'Número :',unique=True)
    nombre=models.CharField(max_length='125', verbose_name=u'Nombre Cliente:')
    factura=models.CharField(max_length='125', verbose_name=u'Numero Factura')
    vendedor=models.CharField(max_length='250', verbose_name=u'Vendedor:')
    usuario_creador = models.ForeignKey(User,null=True,blank=True)
    fecha_creacion = models.DateField(auto_now=False)
    comentario=models.TextField(max_length='250', verbose_name=u'Comentario:')
    total=models.DecimalField(max_digits=10,decimal_places=2,verbose_name=u'Total')
    def __unicode__(self):
        return '%s - %s - %s' % (self.numero, self.nombre,self.total)

class ProductosNota(models.Model):
    nombreProducto= models.CharField(max_length='125', verbose_name=u'Nombre Producto:')
    unidades = models.IntegerField(verbose_name=u'Unidades:')
    precio=models.DecimalField(max_digits=10,decimal_places=2,verbose_name=u'Precio Unitario')
    descuento=models.DecimalField(max_digits=10,decimal_places=2,verbose_name=u'Descuento')
    fecha = models.DateField(auto_now=False)
    total=models.DecimalField(max_digits=10,decimal_places=2,verbose_name=u'Total')
    def __unicode__(self):
        return '%s - %s -%s - %s' % (self.nombreProducto, self.unidades,self.precio,self.total)

class NotaCreditoProductosNota(models.Model):
    id_notacredito = models.ForeignKey(NotaCredito)
    id_producto = models.ForeignKey(ProductosNota)
    def __unicode__(self):
        return u'%s %s' % (self.id_notacredito, self.id_producto)

#nota debito

class NotaDebito(models.Model):
    RAZON=(
        ('Facturación inferior a la debida','Facturación inferior a la debida'),
        ('Gastos por envíos.','Gastos por envíos.'),
        ('Comisiones bancarias','Comisiones bancarias'),
        ('InteresesError en menos en la facturación.','InteresesError en menos en la facturación.')
    )
    numero=models.CharField(max_length='125',verbose_name=u'Número :',unique=True)
    nombre=models.CharField(max_length='125', verbose_name=u'Nombre Cliente:')
    factura=models.CharField(max_length='125', verbose_name=u'Numero Factura')
    vendedor=models.CharField(max_length='250', verbose_name=u'Vendedor:')
    razon1 = models.CharField(max_length='2', verbose_name=u'Detalle 1 :', choices = RAZON)
    subtotal1=models.DecimalField(max_digits=10,decimal_places=2,verbose_name=u'SubTotal 1')
    razon2 = models.CharField(max_length='2', verbose_name=u'Detalle 2 :', choices = RAZON)
    subtotal2=models.DecimalField(max_digits=10,decimal_places=2,verbose_name=u'SubTotal 2')
    usuario_creador = models.ForeignKey(User,null=True,blank=True)
    fecha_creacion = models.DateField(auto_now=False)
    comentario=models.TextField(max_length='250', verbose_name=u'Comentario:')
    total=models.DecimalField(max_digits=10,decimal_places=2,verbose_name=u'Total')
    def __unicode__(self):
        return '%s - %s - %s' % (self.numero, self.nombre,self.total)

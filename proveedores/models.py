# -*- coding: utf8 -*-
from django.db import models
from django.contrib.auth.models import User
from empleados.models import Empleado
from django.db.models import ImageField

class Proveedor(models.Model):
    CREDITO=(
        ('SI','SI'),
        ('NO','NO'),
    )
    ESTADO=(
        ('SI','SI'),
        ('NO','NO'),
    )
    codigo=models.CharField(max_length='125',verbose_name=u'Código :',unique=True)
    nombre= models.CharField(max_length='125', verbose_name=u'Nombre Proveedor:')
    tel_proveedor = models.IntegerField(null=True, blank=True,verbose_name=u'Teléfono Empresa:')
    n_contacto=models.CharField(null=True, blank=True,max_length='50', verbose_name=u'Nombre Contacto:')
    tel_contacto = models.IntegerField(null=True, blank=True, verbose_name=u'Teléfono Contacto:')
    direccion=models.TextField(max_length='250', verbose_name=u'Dirección:')
    pais=models.CharField(max_length='25', verbose_name=u'País Ubicación:')
    credito = models.CharField(max_length='2', verbose_name=u'Crédito :', choices = CREDITO)
    habilitado = models.CharField(max_length='2', verbose_name=u'Habilitado :', choices = ESTADO)
    def __unicode__(self):
        return '%s - %s - %s' % (self.codigo, self.nombre,self.tel_proveedor)



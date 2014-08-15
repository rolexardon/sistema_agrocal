# -*- coding: utf8 -*-
from django.db import models
from django.contrib.auth.models import User



class Empleado(models.Model):
    GENEROS = (
        ('F','FEMENINO'),
        ('M','MASCULINO'),
    )
    TIPOS = (
        ('Vendedor','Vendedor'),
        ('Administrador','Administrador'),
        ('Gerencia','Gerencia'),
    )
    ESTADO_CIVIL = (
        ('Soltero','Soltero'),
        ('Casado','Casado'),
        ('Viudo','Viudo'),
    )
    ESTADO=(
        ('SI','SI'),
        ('NO','NO'),
    )
    identidad = models.CharField(max_length='15', verbose_name=u'Número de Identidad :',unique=True)
    p_nombre = models.CharField(max_length='125', verbose_name=u'Primer Nombre :')
    s_nombre = models.CharField(max_length='125', verbose_name=u'Segundo Nombre :', blank=True)
    p_apellido = models.CharField(max_length='125', verbose_name=u'Primer Apellido :')
    s_apellido = models.CharField(max_length='125', verbose_name=u'Segundo Apellido :', blank=True)
    genero = models.CharField(max_length='1', verbose_name=u'Género :', choices = GENEROS)
    tipo = models.CharField(max_length='1', verbose_name=u'Tipo Empleado :', choices = TIPOS)
    f_nacimiento = models.DateField(verbose_name=u'Fecha Nacimiento :')
    e_civil = models.CharField(max_length='1', verbose_name=u'Estado Civil :', choices = ESTADO_CIVIL)
    direccion=models.TextField(max_length='250', verbose_name=u'Dirección:')
    t_fijo = models.IntegerField(null=True,blank=True, verbose_name=u'Teléfono Fijo:')
    t_movil = models.IntegerField(null=True,blank=True, verbose_name=u'Teléfono Movil:')
    habilitado = models.CharField(max_length='2', verbose_name=u'Habilitado :', choices = ESTADO)
    usuario_creador = models.ForeignKey(User, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '[ %s ] - %s %s' % (self.identidad, self.p_nombre, self.p_apellido)

class Facturas(models.Model):
    talonario=models.CharField(max_length='15', verbose_name=u'Número de Talonario :',unique=False)
    factura=models.CharField(max_length='15', verbose_name=u'Número de Factura :',unique=False)
    estado=models.CharField(max_length='3', verbose_name=u'estado :')
    empleado=models.ForeignKey(Empleado)
    def __unicode__(self):
        return 'Factura:%s Empleado%s' % (self.factura,self.empleado)





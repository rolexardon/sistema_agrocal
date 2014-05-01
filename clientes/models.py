# -*- coding: utf8 -*-
from django.db import models
from django.contrib.auth.models import User
from empleados.models import Empleado
from django.db.models import ImageField

class Cliente(models.Model):
    TIPO_VENTA = (
        ('Contado','CONTADO'),
        ('Credito','CREDITO'),
        ('Ambas','CONTADO-CREDITO'),
    )
    ESTADO=(
        ('SI','SI'),
        ('NO','NO'),
    )
    PREFERENCIA=(
        ('SI','SI'),
        ('NO','NO'),
    )
    codigo=models.CharField(max_length='125',unique=True, verbose_name=u'Código :')
    identidad = models.CharField(max_length='125',null=True,blank=True, verbose_name=u'Identidad :')
    rnt = models.CharField(max_length='125',null=True,blank=True, verbose_name=u'RTN :')
    nombre_cliente = models.CharField(max_length='125', verbose_name=u'Nombre Cliente :')
    tel1 = models.IntegerField(null=True,blank=True, verbose_name=u'Teléfono 1:')
    tel2 = models.IntegerField(null=True,blank=True, verbose_name=u'Teléfono 2:')
    tel3 = models.IntegerField(null=True,blank=True, verbose_name=u'Teléfono 3:')
    tel4 = models.IntegerField(null=True,blank=True, verbose_name=u'Teléfono 4:')
    tel5 = models.IntegerField(null=True,blank=True, verbose_name=u'Teléfono 5:')
    tel6 = models.IntegerField(null=True,blank=True, verbose_name=u'Teléfono 6:')
    direccion=models.TextField(max_length='250', verbose_name=u'Dirección:')
    tipo = models.CharField(max_length='1', verbose_name=u'Tipo de Venta :', choices = TIPO_VENTA)
    correo = models.EmailField(null=True,blank=True,verbose_name=u'Email :')
    vendedor = models.ForeignKey(Empleado)
    n_contacto=models.CharField(null=True,blank=True,max_length='50', verbose_name=u'Nombre Contacto:')
    tel_contacto = models.IntegerField(null=True,blank=True, verbose_name=u'Teléfono Contacto:')
    limite_credito=models.DecimalField(null=True,blank=True,max_digits=10,decimal_places=2,verbose_name=u'Limite de Credito')
    habilitado = models.CharField(max_length='2', verbose_name=u'Habilitado :', choices = ESTADO)
    preferencial = models.CharField(max_length='2', verbose_name=u'Preferencial :', choices = PREFERENCIA)
    firma= models.ImageField(upload_to="imagen_clientes/",null=True,blank=True)
    usuario_creador = models.ForeignKey(User, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return '[ %s ] - %s ' % (self.identidad, self.nombre_cliente)

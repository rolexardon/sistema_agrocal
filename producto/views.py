# -*- coding: utf8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.db import transaction
from django.http import HttpResponse

from django.shortcuts import render
from producto.models import Producto
from producto.models import PromocionProducto


def gestion_producto(request):
    ddic = {}
    if not request.user.is_authenticated():
        return render_to_response('account_login.html',ddic,context_instance=RequestContext(request))
    ddic['producto'] = Producto.objects.all().filter(habilitado='SI').order_by('nombre')
    return render_to_response('productos_main.html',ddic,context_instance=RequestContext(request))

def detalle_producto(request,mod_id=None):
    ddic = {}
    if not request.user.is_authenticated():
        return render_to_response('account_login.html',ddic,context_instance=RequestContext(request))
    ddic['producto'] = Producto.objects.get(pk=mod_id)
    return render_to_response('productos_detalle.html',ddic,context_instance=RequestContext(request))

def busca_producto(request):
    ddic = {}
    if not request.user.is_authenticated():
        return render_to_response('account_login.html',ddic,context_instance=RequestContext(request))
    nombre = request.GET['nombre']
    ddic['producto'] = Producto.objects.filter(nombre__contains=nombre,habilitado='SI')
    return render_to_response('productos_main.html',ddic,context_instance=RequestContext(request))

def gestion_promocion(request):
    ddic = {}
    if not request.user.is_authenticated():
        return render_to_response('account_login.html',ddic,context_instance=RequestContext(request))
    ddic['promocion'] = PromocionProducto.objects.all().filter(habilitado='SI').order_by('nombre_promocion')
    return render_to_response('promocion_main.html',ddic,context_instance=RequestContext(request))

def detalle_promocion(request,mod_id=None):
    ddic = {}
    if not request.user.is_authenticated():
        return render_to_response('account_login.html',ddic,context_instance=RequestContext(request))
    ddic['producto'] = Producto.objects.get(pk=mod_id)
    return render_to_response('promocion_detalle.html',ddic,context_instance=RequestContext(request))

def busca_promocion(request):
    ddic = {}
    if not request.user.is_authenticated():
        return render_to_response('account_login.html',ddic,context_instance=RequestContext(request))
    nombre = request.GET['nombre']
    try :
        pro=Producto.objects.all().filter(habilitado='SI',nombre__contains=nombre)
        for a in pro:
            ddic['promocion'] = PromocionProducto.objects.all().filter(habilitado='SI',id_producto=a.pk)
    except  Producto . DoesNotExist :
        ddic['error']= {'message':u'No Existe alguna promocion para el producto buscado'}
    return render_to_response('promocion_main.html',ddic,context_instance=RequestContext(request))
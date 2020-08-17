# -*- coding: utf8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.db import transaction
from django.http import HttpResponse

from django.shortcuts import render
from proveedores.models import Proveedor


def gestion_proveedor(request):
    ddic = {}
    if not request.user.is_authenticated():
        return render_to_response('account_login.html',ddic,context_instance=RequestContext(request))
    ddic['proveedor'] = Proveedor.objects.filter(habilitado='SI').order_by('nombre')
    return render_to_response('proveedores_main.html',ddic,context_instance=RequestContext(request))

def detalle_proveedor(request,mod_id=None):
    ddic = {}
    if not request.user.is_authenticated():
        return render_to_response('account_login.html',ddic,context_instance=RequestContext(request))
    ddic['proveedor'] = Proveedor.objects.get(pk=mod_id)
    return render_to_response('proveedores_detalle.html',ddic,context_instance=RequestContext(request))

def busca_proveedor(request):
    ddic = {}
    if not request.user.is_authenticated():
        return render_to_response('account_login.html',ddic,context_instance=RequestContext(request))
    nombre = request.GET['nombre']
    ddic['proveedor'] = Proveedor.objects.filter(nombre__contains=nombre,habilitado='SI')
    return render_to_response('proveedores_main.html',ddic,context_instance=RequestContext(request))

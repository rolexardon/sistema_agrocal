# -*- coding: utf8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.db import transaction
from django.http import HttpResponse

from django.shortcuts import render
from clientes.models import Cliente


def gestion_cliente(request):
    ddic = {}
    if not request.user.is_authenticated():
        return render_to_response('account_login.html',ddic,context_instance=RequestContext(request))
    ddic['cliente'] = Cliente.objects.all().filter(habilitado='SI').order_by('nombre_cliente')
    return render_to_response('clientes_main.html',ddic,context_instance=RequestContext(request))

def detalle_cliente(request,mod_id=None):
    ddic = {}
    if not request.user.is_authenticated():
        return render_to_response('account_login.html',ddic,context_instance=RequestContext(request))
    ddic['cliente'] = Cliente.objects.get(pk=mod_id)
    return render_to_response('clientes_detalle.html',ddic,context_instance=RequestContext(request))

def busca_cliente(request):
    ddic = {}
    if not request.user.is_authenticated():
        return render_to_response('account_login.html',ddic,context_instance=RequestContext(request))
    nombre = request.GET['nombre']
    ddic['cliente'] = Cliente.objects.filter(nombre_cliente__contains=nombre,habilitado='SI')
    return render_to_response('clientes_main.html',ddic,context_instance=RequestContext(request))
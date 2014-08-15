# -*- coding: utf8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.db import transaction
from django.http import HttpResponse
from empleados.models import *

from django.shortcuts import render

from empleados.forms import Empleado,EmpleadoForm


def gestion_empleado(request):
    ddic = {}
    if not request.user.is_authenticated():
        return render_to_response('account_login.html',ddic,context_instance=RequestContext(request))
    ddic['empleado'] = Empleado.objects.all().filter(habilitado='SI').order_by('p_nombre','p_apellido')
    return render_to_response('empleado_main.html',ddic,context_instance=RequestContext(request))

def gestion_talonarios(request):
    ddic = {}
    if not request.user.is_authenticated():
        return render_to_response('account_login.html',ddic,context_instance=RequestContext(request))
    ddic['empleado'] = Empleado.objects.all().filter(habilitado='SI').order_by('p_nombre','p_apellido')
    return render_to_response('empleado_talonario.html',ddic,context_instance=RequestContext(request))


def talonario_crear(request):
    #Revisar permisos para esta accion
    ddic = {}
    if not request.user.is_authenticated():
        return render_to_response('account_login.html',ddic,context_instance=RequestContext(request))
    errores =[]

    ddic['empleados'] = Empleado.objects.all().filter(habilitado='SI').order_by('p_nombre')
    ddic['facturas'] = Facturas.objects.all().order_by('numero')

    if request.method == 'GET':
        return render_to_response('empleado_talonario.html',ddic, context_instance=RequestContext(request))
    elif request.method == 'POST':
        #TALONARIO
        ddic['empleado'] = request.POST.get('nombre')
        ddic['numero'] = request.POST.get('numero')
        d = int(request.POST.get('desde'))
        h = int(request.POST.get('hasta'))
        for e in ddic['empleados']:
            if int(e.pk)==int(ddic['empleado']):
                r=e
        for f in range (d,h+1):
            talonario=Facturas.objects.create(talonario=int(ddic['numero']),factura=f,estado='P',empleado=r)
        ddic['empleados'] = Empleado.objects.all().filter(habilitado='SI').order_by('p_nombre')
        if errores:
            ddic['error'] = {'message':'Se han detectado errores %s' % (errores)}
            return render_to_response('empleado_talonario.html',ddic,context_instance=RequestContext(request))
        else:
            ddic['success'] = {'message':u'Se ingreso con exito la información.'}
            return render_to_response('empleado_talonario.html',ddic, context_instance=RequestContext(request))



def empleado_crear(request):
    #Revisar permisos para esta accion
    ddic = {}
    if not request.user.is_authenticated():
        return render_to_response('account_login.html',ddic,context_instance=RequestContext(request))
    ddic['modify'] = False
    if request.method == 'GET':
        emp_form = EmpleadoForm()
        ddic['emp_form'] = emp_form
        return render_to_response('empleado_admin.html',ddic, context_instance=RequestContext(request))
    elif request.method == 'POST':
        emp_form = EmpleadoForm(request.POST)
        ddic['emp_form'] = emp_form
        if emp_form.is_valid():
            tmp_per_form = emp_form.save(commit = False)
            tmp_per_form.usuario_creador = request.user
            tmp_per_form.save()
            ddic['success'] = {'message':u'Se ingreso con exito la informacion.'}
            ddic['empleado'] = Empleado.objects.all().order_by('p_nombre','p_apellido')
            return render_to_response('empleado_main.html',ddic,context_instance=RequestContext(request))
        else:
            ddic['error']= {'message':u'Han ocurrido errores porfavor revise la información ingresada.'}
            return render_to_response('empleado_admin.html',ddic, context_instance=RequestContext(request))

def empleado_modificar(request, mod_id=None):
    ddic = {}
    if not request.user.is_authenticated():
        return render_to_response('account_login.html',ddic,context_instance=RequestContext(request))
    ddic['modify'] = True
    ddic['mod_id'] = mod_id
    emp = get_object_or_404(Empleado, pk=mod_id)
    if request.method == 'GET':
        emp_form = EmpleadoForm(instance=emp)
        ddic.update({'emp_form':emp_form})
        return render_to_response('empleado_admin.html',ddic, context_instance=RequestContext(request))
    elif request.method == 'POST':
        emp_form = EmpleadoForm(request.POST, instance=emp)
        ddic['emp_form'] = emp_form
        if emp_form.is_valid():
            emp_form.save()
            ddic['success'] = {'message':u'Se ingreso con exito la información.'}
            ddic['empleado'] = Empleado.objects.all().order_by('p_nombre','p_apellido')
            return render_to_response('empleado_main.html',ddic,context_instance=RequestContext(request))
        else:
            ddic['error']= {'message':u'Han ocurrido errores porfavor revise la información ingresada.'}
            return render_to_response('empleado_admin.html',ddic, context_instance=RequestContext(request))

def empleado_buscar(request):
    ddic = {}
    if not request.user.is_authenticated():
        return render_to_response('account_login.html',ddic,context_instance=RequestContext(request))
    nombre = request.GET['nombre']
    ddic['empleado'] = Empleado.objects.filter(p_nombre__contains=nombre,habilitado='SI')|Empleado.objects.filter(p_apellido__contains=nombre,habilitado='SI')
    return render_to_response('empleado_main.html',ddic,context_instance=RequestContext(request))

def detalle_empleado(request,mod_id=None):
    ddic = {}
    if not request.user.is_authenticated():
        return render_to_response('account_login.html',ddic,context_instance=RequestContext(request))
    ddic['empleado'] = Empleado.objects.get(pk=mod_id)
    ddic['facturaspendientes']=Facturas.objects.all().filter(estado='P',empleado=ddic['empleado'])
    ddic['facturasusadas']=Facturas.objects.all().filter(estado='A',empleado=ddic['empleado'])
    return render_to_response('empleado_detalle.html',ddic,context_instance=RequestContext(request))

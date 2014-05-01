# -*- coding: utf8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.db.models import Count,Min,Sum,Avg
from django.http import HttpResponse
from datetime import timedelta
from django.shortcuts import render
from producto.models import Producto
from factura.models import *
from proveedores.models import *


def gestion_reporte(request):
    ddic = {}
    ddic['producto'] = Producto.objects.all().order_by('nombre')
    return render_to_response('reportes_main.html',ddic,context_instance=RequestContext(request))


def proveedorproductos_reporte(request):
    ddic = {}
    ddic['proveedores'] = Producto.objects.values('proveedor').annotate(cantidad_productos=Count('codigo'))
    ddic['proveedor'] = Proveedor.objects.all()
    print(ddic['proveedores'])
    return render_to_response('reportes_proveedorproductos.html',ddic,context_instance=RequestContext(request))

def productosvendidos_reporte(request):
    ddic = {}
    return render_to_response('reportes_productosvendidos.html',ddic,context_instance=RequestContext(request))

def productosvendidosfecha_reporte(request):
    ddic = {}
    fechai=request.GET['fechainicio']
    fechaf= request.GET['fechafin']
    ddic['producto'] = Productos.objects.values('nombreProducto').annotate(total_venta=Sum('unidades')).filter(fecha__gte=fechai,fecha__lte=fechaf)
    return render_to_response('reportes_productosvendidos.html',ddic,context_instance=RequestContext(request))

#FACTURAS POR CLIENTE

def clientes_reporte(request):
    ddic = {}
    return render_to_response('reportes_clientes.html',ddic,context_instance=RequestContext(request))

def clientesfecha_reporte(request):
    ddic = {}
    fechai=request.GET['fechainicio']
    fechaf= request.GET['fechafin']
    ddic['clientes'] = Factura.objects.values('nombre').annotate(cantidad_facturas=Count('total'),total_facturado=Sum('total')).filter(fecha_creacion__gte=fechai,fecha_creacion__lte=fechaf)
    print(ddic['clientes'])
    return render_to_response('reportes_clientes.html',ddic,context_instance=RequestContext(request))

#NOTAS DE CREDITO POR CLIENTE

def clientes_creditomain(request):
    ddic = {}
    return render_to_response('reportes_creditoclientes.html',ddic,context_instance=RequestContext(request))


def clientes_credito(request):
    ddic = {}
    ddic['titulo'] = "Reporte Notas Credito Clientes"
    fechai=request.GET['fechainicio']
    fechaf= request.GET['fechafin']
    ddic['clientes'] = NotaCredito.objects.values('nombre').annotate(cantidad_notas=Count('total'),total_notas=Sum('total')).filter(fecha_creacion__gte=fechai,fecha_creacion__lte=fechaf)
    print(ddic['clientes'])
    return render_to_response('reportes_creditoclientes.html',ddic,context_instance=RequestContext(request))

#NOTAS DE DEBITO POR CLIENTE

def clientes_debitomain(request):
    ddic = {}
    return render_to_response('reportes_debitoclientes.html',ddic,context_instance=RequestContext(request))


def clientes_debito(request):
    ddic = {}
    ddic['titulo'] = "Reporte Notas Debito Clientes"
    fechai=request.GET['fechainicio']
    fechaf= request.GET['fechafin']
    ddic['clientes'] = NotaDebito.objects.values('nombre').annotate(cantidad_notas=Count('total'),total_notas=Sum('total')).filter(fecha_creacion__gte=fechai,fecha_creacion__lte=fechaf)
    print(ddic['clientes'])
    return render_to_response('reportes_debitoclientes.html',ddic,context_instance=RequestContext(request))

#VENDEDORES

def vendedores_reporte(request):
    ddic = {}
    return render_to_response('reportes_ventasvendedor.html',ddic,context_instance=RequestContext(request))


def vendedoresfecha_reporte(request):
    ddic = {}
    fechai=request.GET['fechainicio']
    fechaf= request.GET['fechafin']
    ddic['vendedor'] = Factura.objects.values('vendedor').annotate(cantidad_ventas=Count('total'),total_ventas=Sum('total')).filter(fecha_creacion__gte=fechai,fecha_creacion__lte=fechaf)
    print(ddic['vendedor'])
    return render_to_response('reportes_ventasvendedor.html',ddic,context_instance=RequestContext(request))




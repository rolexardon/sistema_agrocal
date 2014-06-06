# -*- coding: utf8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.db import transaction
from django.http import HttpResponse

from django.shortcuts import render
from proveedores.models import Proveedor
from empleados.models import Empleado
from producto.models import Producto,PromocionProducto
from clientes.models import Cliente
from factura.models import NotaDebito,Factura,Impuesto,Productos,ProductosFactura,NotaCredito,ProductosNota,NotaCreditoProductosNota,NotaDebito


def gestion_proveedor(request):
    ddic = {}
    if not request.user.is_authenticated():
        return render_to_response('account_login.html',ddic,context_instance=RequestContext(request))
    ddic['proveedor'] = Proveedor.objects.all().filter(habilitado='SI').order_by('nombre')
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

def ingreso_crear(request):
    #Revisar permisos para esta accion
    ddic = {}
    if not request.user.is_authenticated():
        return render_to_response('account_login.html',ddic,context_instance=RequestContext(request))
    errores =[]
    ddic['clientes'] = Cliente.objects.all().filter(habilitado='SI').order_by('nombre_cliente')
    ddic['empleados'] = Empleado.objects.all().filter(habilitado='SI').order_by('p_nombre')
    ddic['productos'] = Producto.objects.all().filter(habilitado='SI').order_by('nombre')
    ddic['nota'] = NotaCredito.objects.all().order_by('numero')
    ddic['facturas'] = Factura.objects.all().order_by('nombre','numero')

    if request.method == 'GET':
        return render_to_response('ingreso_crear.html',ddic, context_instance=RequestContext(request))
    elif request.method == 'POST':
        #FACTURA

        ddic['numero'] = request.POST.get('numero')
        ddic['nombre'] = request.POST.get('nombre')
        ddic['fecha'] = request.POST.get('fecha')
        ddic['vendedor'] = request.POST.get('vendedor')
        ddic['factura'] = request.POST.get('factura')
        ddic['subtotal'] = request.POST.get('subtotal')
        ddic['comentario']= request.POST.get('comentario')
        ddic['total'] = request.POST.get('total')
        for a in ddic['nota']:
            if a.numero == ddic['numero']:
                errores.append('El sistema encontro una Nota de Credito existente con el mismo numero')
        #PRODUCTOS

        ddic['unidades1'] = request.POST.get('unidades1')
        ddic['producto1'] = request.POST.get('producto1')
        ddic['precio1'] = request.POST.get('precio1')
        ddic['total1'] = request.POST.get('total1')

        ddic['unidades2'] = request.POST.get('unidades2')
        ddic['producto2'] = request.POST.get('producto2')
        ddic['precio2'] = request.POST.get('precio2')
        ddic['total2'] = request.POST.get('total2')

        ddic['unidades3'] = request.POST.get('unidades3')
        ddic['producto3'] = request.POST.get('producto3')
        ddic['precio3'] = request.POST.get('precio3')
        ddic['total3'] = request.POST.get('total3')

        ddic['unidades4'] = request.POST.get('unidades4')
        ddic['producto4'] = request.POST.get('producto4')
        ddic['precio4'] = request.POST.get('precio4')
        ddic['total4'] = request.POST.get('total4')

        ddic['unidades5'] = request.POST.get('unidades5')
        ddic['producto5'] = request.POST.get('producto5')
        ddic['precio5'] = request.POST.get('precio5')
        ddic['total5'] = request.POST.get('total5')

        ddic['unidades6'] = request.POST.get('unidades6')
        ddic['producto6'] = request.POST.get('producto6')
        ddic['precio6'] = request.POST.get('precio6')
        ddic['total6'] = request.POST.get('total6')

        ddic['unidades7'] = request.POST.get('unidades7')
        ddic['producto7'] = request.POST.get('producto7')
        ddic['precio7'] = request.POST.get('precio7')
        ddic['total7'] = request.POST.get('total7')

        ddic['unidades8'] = request.POST.get('unidades8')
        ddic['producto8'] = request.POST.get('producto8')
        ddic['precio8'] = request.POST.get('precio8')
        ddic['total8'] = request.POST.get('total8')

        ddic['unidades9'] = request.POST.get('unidades9')
        ddic['producto9'] = request.POST.get('producto9')
        ddic['precio9'] = request.POST.get('precio9')
        ddic['total9'] = request.POST.get('total9')

        ddic['unidades10'] = request.POST.get('unidades10')
        ddic['producto10'] = request.POST.get('producto10')
        ddic['precio10'] = request.POST.get('precio10')
        ddic['total10'] = request.POST.get('total10')

        ddic['unidades11'] = request.POST.get('unidades11')
        ddic['producto11'] = request.POST.get('producto11')
        ddic['precio11'] = request.POST.get('precio11')
        ddic['total11'] = request.POST.get('total11')

        ddic['unidades12'] = request.POST.get('unidades12')
        ddic['producto12'] = request.POST.get('producto12')
        ddic['precio12'] = request.POST.get('precio12')
        ddic['total12'] = request.POST.get('total12')

        ddic['unidades13'] = request.POST.get('unidades13')
        ddic['producto13'] = request.POST.get('producto13')
        ddic['precio13'] = request.POST.get('precio13')
        ddic['total13'] = request.POST.get('total13')

        ddic['unidades14'] = request.POST.get('unidades14')
        ddic['producto14'] = request.POST.get('producto14')
        ddic['precio14'] = request.POST.get('precio14')
        ddic['total14'] = request.POST.get('total14')

        ddic['unidades15'] = request.POST.get('unidades15')
        ddic['producto15'] = request.POST.get('producto15')
        ddic['precio15'] = request.POST.get('precio15')
        ddic['total15'] = request.POST.get('total15')

        listaproductos=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        if errores:
            ddic['error'] = {'message':'Se han detectado errores %s' % (errores)}
            return render_to_response('ingreso_crear.html',ddic,context_instance=RequestContext(request))
        else:

            Nota=NotaCredito.objects.create(numero=ddic['numero'],fecha_creacion=ddic['fecha'],nombre=ddic['nombre'],comentario=ddic['comentario'],vendedor=ddic['vendedor'],total=Decimal('%.2f' % float(ddic['total'])))

            for x in listaproductos:

                if ddic['producto'+str(x)] !=  "SIN NOMBRE":
                    for y in ddic['productos']:

                        if y.nombre == ddic['producto'+str(x)]:
                            y.cantidad=y.cantidad+int(ddic['unidades'+str(x)])
                            y.save()
                    ProductosNota1=ProductosNota.objects.create(nombreProducto=ddic['producto'+str(x)],unidades=ddic['unidades'+str(x)],precio=ddic['precio'+str(x)],descuento=0,fecha=ddic['fecha'],total=ddic['total'+str(x)])
                    NotaCreditoProductosNota.objects.create(id_notacredito=Nota,id_producto=ProductosNota1)


            ddic['success'] = {'message':u'Se ingreso con exito la información.'}
            return render_to_response('ingreso_crear.html',ddic, context_instance=RequestContext(request))

    return render_to_response('proveedores_main.html',ddic,context_instance=RequestContext(request))


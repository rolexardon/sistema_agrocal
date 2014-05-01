# -*- coding: utf8 -*-
from factura.models import NotaDebito,Factura,Impuesto,Productos,ProductosFactura,NotaCredito,ProductosNota,NotaCreditoProductosNota,NotaDebito
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.db import transaction
from django.http import HttpResponse
from django.core.context_processors import csrf
from decimal import *

from django.shortcuts import render
from empleados.models import Empleado
from producto.models import Producto,PromocionProducto
from clientes.models import Cliente

def get_ajax(request):
    import json
    if request.is_ajax():
        if request.method == 'GET':
            if request.GET.get('data') == 'getPrecios':
                try:
                    data = []
                    query = {}

                    if request.GET.get('producto','') and request.GET.get('producto','') != '0':
                        query['producto'] = request.GET.get('producto','')
                    print(query['producto'])
                    med = Producto.objects.all().filter(habilitado='SI',nombre=query['producto']).order_by('nombre')
                    data = [{'pk':m.pk,'precio_min': ' %s ' % (m.precio_venta_min),'precio_med': ' %s ' % (m.precio_venta_med),'precio_max': ' %s ' % (m.precio_venta_max)} for m in med]
                    #print(data)
                    return HttpResponse(json.dumps(data), content_type="text/json")
                except Exception, e:
                    print e
                    return HttpResponse(json.dumps([{'error':'Ha ocurrido un error'}]), content_type="text/json")

            if request.GET.get('data') == 'getDescuento':
                try:
                    data = []
                    query = {}
                    if request.GET.get('producto','') and request.GET.get('producto','') != '0':
                        query['producto'] = request.GET.get('producto','')
                    pro=Producto.objects.all().filter(habilitado='SI',nombre=query['producto']).order_by('nombre')
                    for a in pro:
                        query['pk']=a.pk
                    med = PromocionProducto.objects.all().filter(habilitado='SI',id_producto=query['pk'])
                    data = [{'pk':m.pk,'porcentaje_descuento': ' %s ' % (m.porcentaje_descuento)} for m in med]
                    print(data)
                    return HttpResponse(json.dumps(data), content_type="text/json")
                except Exception, e:
                    print e
                    return HttpResponse(json.dumps([{'error':'Ha ocurrido un error'}]), content_type="text/json")

            if request.GET.get('data') == 'getFacturas':
                try:
                    data = []
                    query = {}

                    if request.GET.get('nombre','') and request.GET.get('nombre','') != '0':
                        query['nombre'] = request.GET.get('nombre','')
                    print(query['nombre'])
                    med = Factura.objects.all().filter(nombre__contains=query['nombre']).order_by('numero')
                    data = [{'numero':m.numero,'nombre': ' %s ' % (m.nombre),'total': ' %s ' % (m.total)} for m in med]
                    print(data)
                    return HttpResponse(json.dumps(data), content_type="text/json")
                except Exception, e:
                    print e
                    return HttpResponse(json.dumps([{'error':'Ha ocurrido un error'}]), content_type="text/json")

def gestion_factura(request):
    ddic = {}
    if not request.user.is_authenticated():
        return render_to_response('account_login.html',ddic,context_instance=RequestContext(request))
    ddic['factura'] = Factura.objects.all().order_by('numero')
    return render_to_response('factura_main.html',ddic,context_instance=RequestContext(request))

def factura_crear(request):
    #Revisar permisos para esta accion
    ddic = {}
    if not request.user.is_authenticated():
        return render_to_response('account_login.html',ddic,context_instance=RequestContext(request))
    errores =[]
    ddic['clientes'] = Cliente.objects.all().filter(habilitado='SI').order_by('nombre_cliente')
    ddic['empleados'] = Empleado.objects.all().filter(habilitado='SI').order_by('p_nombre')
    ddic['productos'] = Producto.objects.all().filter(habilitado='SI').order_by('nombre')
    ddic['impuestos'] = Impuesto.objects.all()
    ddic['facturas'] = Factura.objects.all()
    if request.method == 'GET':
        return render_to_response('factura_crear.html',ddic, context_instance=RequestContext(request))
    elif request.method == 'POST':

        #FACTURA

        ddic['numero'] = request.POST.get('numero')
        ddic['nombre'] = request.POST.get('nombre')
        ddic['fecha'] = request.POST.get('fecha')
        ddic['vendedor'] = request.POST.get('vendedor')
        ddic['tipo'] = request.POST.get('tipo')
        ddic['subtotal'] = request.POST.get('subtotal')
        ddic['descuento'] = request.POST.get('descuento')
        ddic['impuesto'] = request.POST.get('impuesto')
        ddic['comentario'] =request.POST.get('comentario')
        ddic['total'] = request.POST.get('total')
        for a in ddic['facturas']:
            if a.numero == ddic['numero']:
                errores.append('El sistema encontro una factura existente con el mismo numero')
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
        for x in listaproductos:
            for y in ddic['productos']:
                if y.nombre == ddic['producto'+str(x)]:
                    if int(y.cantidad) < int(ddic['unidades'+str(x)]):
                        errores.append("Las Unidades ("+ddic['unidades'+str(x)]+") facturadas del Producto: "+ddic['producto'+str(x)]+" son mayores a las existentes ("+ str(y.cantidad)+"), Favor ingrese nuevamente los datos")
        if errores:
            ddic['error'] = {'message':'Se han detectado errores %s' % (errores)}
            return render_to_response('factura_crear.html',ddic,context_instance=RequestContext(request))
        else:

            facturas=Factura.objects.create(numero=ddic['numero'],fecha_creacion=ddic['fecha'],nombre=ddic['nombre'],vendedor=ddic['vendedor'],tipo=ddic['tipo'],subtotal=ddic['subtotal'],impuestoaplicado=ddic['impuesto'],comentario=ddic['comentario'],descuentoaplicado=ddic['descuento'],total=Decimal('%.2f' % float(ddic['total'])))

            for x in listaproductos:
                if ddic['producto'+str(x)] !=  "SIN NOMBRE":
                    for y in ddic['productos']:
                        if y.nombre == ddic['producto'+str(x)]:
							#aqui va desconteo
                            y.cantidad=y.cantidad-int(ddic['unidades'+str(x)])
                            y.save()
                    productofactura1=Productos.objects.create(nombreProducto=ddic['producto'+str(x)],unidades=ddic['unidades'+str(x)],precio=ddic['precio'+str(x)],descuento=0,fecha=ddic['fecha'],total=ddic['total'+str(x)])
                    ProductosFactura.objects.create(id_factura=facturas,id_producto=productofactura1)


            ddic['success'] = {'message':u'Se ingreso con exito la información.'}
            return render_to_response('factura_crear.html',ddic, context_instance=RequestContext(request))

def factura_buscar(request):
    ddic = {}
    if not request.user.is_authenticated():
        return render_to_response('account_login.html',ddic,context_instance=RequestContext(request))
    nombre = request.GET['nombre']
    ddic['factura'] = Factura.objects.filter(nombre__contains=nombre).order_by('numero')
    return render_to_response('factura_main.html',ddic,context_instance=RequestContext(request))

def detalle_factura(request,mod_id=None):
    ddic = {}
    if not request.user.is_authenticated():
        return render_to_response('account_login.html',ddic,context_instance=RequestContext(request))
    ddic['factura'] = Factura.objects.get(pk=mod_id)
    ddic['productosfactura']=ProductosFactura.objects.all().filter(id_factura=mod_id)
    return render_to_response('factura_detalle.html',ddic,context_instance=RequestContext(request))


#nota de credito

def gestion_credito(request):
    ddic = {}
    if not request.user.is_authenticated():
        return render_to_response('account_login.html',ddic,context_instance=RequestContext(request))
    ddic['nota'] = NotaCredito.objects.all().order_by('numero')
    return render_to_response('notacredito_main.html',ddic,context_instance=RequestContext(request))


def credito_crear(request):
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
        return render_to_response('notacredito_crear.html',ddic, context_instance=RequestContext(request))
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
            return render_to_response('NotaCredito_crear.html',ddic,context_instance=RequestContext(request))
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
            return render_to_response('NotaCredito_crear.html',ddic, context_instance=RequestContext(request))


def credito_buscar(request):
    ddic = {}
    if not request.user.is_authenticated():
        return render_to_response('account_login.html',ddic,context_instance=RequestContext(request))
    nombre = request.GET['nombre']
    ddic['nota'] = NotaCredito.objects.filter(nombre__contains=nombre).order_by('numero')
    return render_to_response('notacredito_main.html',ddic,context_instance=RequestContext(request))

def detalle_credito(request,mod_id=None):
    ddic = {}
    if not request.user.is_authenticated():
        return render_to_response('account_login.html',ddic,context_instance=RequestContext(request))
    ddic['nota'] = NotaCredito.objects.get(pk=mod_id)
    ddic['ProductosNota']=NotaCreditoProductosNota.objects.all().filter(id_notacredito=mod_id)
    return render_to_response('notacredito_detalle.html',ddic,context_instance=RequestContext(request))

#nota de debito

def gestion_debito(request):
    ddic = {}
    if not request.user.is_authenticated():
        return render_to_response('account_login.html',ddic,context_instance=RequestContext(request))
    ddic['nota'] = NotaDebito.objects.all().order_by('numero')
    return render_to_response('notadebito_main.html',ddic,context_instance=RequestContext(request))


def debito_crear(request):
    #Revisar permisos para esta accion
    ddic = {}
    if not request.user.is_authenticated():
        return render_to_response('account_login.html',ddic,context_instance=RequestContext(request))
    errores =[]
    ddic['clientes'] = Cliente.objects.all().filter(habilitado='SI').order_by('nombre_cliente')
    ddic['empleados'] = Empleado.objects.all().filter(habilitado='SI').order_by('p_nombre')
    ddic['productos'] = Producto.objects.all().filter(habilitado='SI').order_by('nombre')
    ddic['nota'] = NotaDebito.objects.all().order_by('numero')
    ddic['facturas'] = Factura.objects.all().order_by('nombre','numero')

    if request.method == 'GET':
        return render_to_response('notadebito_crear.html',ddic, context_instance=RequestContext(request))
    elif request.method == 'POST':
        #FACTURA

        ddic['numero'] = request.POST.get('numero')
        ddic['nombre'] = request.POST.get('nombre')
        ddic['fecha'] = request.POST.get('fecha')
        ddic['vendedor'] = request.POST.get('vendedor')
        ddic['factura'] = request.POST.get('factura')
        ddic['subtotal1'] = request.POST.get('subtotal1')
        ddic['subtotal2'] = request.POST.get('subtotal2')
        ddic['razon1'] = request.POST.get('razon1')
        ddic['razon2'] = request.POST.get('razon2')
        ddic['comentario'] = request.POST.get('comentario')
        ddic['total'] = request.POST.get('total')
        for a in ddic['nota']:
            if a.numero == ddic['numero']:
                errores.append('El sistema encontro una Nota de Debito existente con el mismo numero')
        #razones

        if errores:
            ddic['error'] = {'message':'Se han detectado errores %s' % (errores)}
            return render_to_response('notadebito_crear.html',ddic,context_instance=RequestContext(request))
        else:

            Nota=NotaDebito.objects.create(numero=ddic['numero'],fecha_creacion=ddic['fecha'],comentario=ddic['comentario'],nombre=ddic['nombre'],vendedor=ddic['vendedor'],razon1=ddic['razon1'],razon2=ddic['razon2'],subtotal1=ddic['subtotal1'],subtotal2=ddic['subtotal2'],total=Decimal('%.2f' % float(ddic['total'])))
            ddic['success'] = {'message':u'Se ingreso con exito la información.'}
            return render_to_response('notadebito_crear.html',ddic, context_instance=RequestContext(request))


def debito_buscar(request):
    ddic = {}
    if not request.user.is_authenticated():
        return render_to_response('account_login.html',ddic,context_instance=RequestContext(request))
    nombre = request.GET['nombre']
    ddic['nota'] = NotaDebito.objects.filter(nombre__contains=nombre).order_by('numero')
    return render_to_response('notadebito_main.html',ddic,context_instance=RequestContext(request))

def detalle_debito(request,mod_id=None):
    ddic = {}
    if not request.user.is_authenticated():
        return render_to_response('account_login.html',ddic,context_instance=RequestContext(request))
    ddic['nota'] = NotaDebito.objects.get(pk=mod_id)
    return render_to_response('notadebito_detalle.html',ddic,context_instance=RequestContext(request))

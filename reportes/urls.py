# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('reportes.views',

    url(r"^$", "gestion_reporte", name="gestion_reporte"),
    url(r"^productos_ventas", "productosvendidos_reporte", name="productosvendidos_reporte"),
    url(r"^productos_fecha", "productosvendidosfecha_reporte", name="productosvendidosfecha_reporte"),

    url(r"^proveedor_productos", "proveedorproductos_reporte", name="proveedorproductos_reporte"),


    url(r"^clientes_ventas", "clientes_reporte", name="clientes_reporte"),
    url(r"^clientes_fecha", "clientesfecha_reporte", name="clientesfecha_reporte"),
    url(r"^clientes_credito", "clientes_credito", name="clientes_credito"),
    url(r"^clientes_debito", "clientes_debito", name="clientes_debito"),
    url(r"^mainclientes_credito", "clientes_creditomain", name="clientes_creditomain"),
    url(r"^mainclientes_debito", "clientes_debitomain", name="clientes_debitomain"),


    url(r"^vendedores_ventas", "vendedores_reporte", name="vendedores_reporte"),
    url(r"^vendedores_fecha", "vendedoresfecha_reporte", name="vendedoresfecha_reporte"),






)
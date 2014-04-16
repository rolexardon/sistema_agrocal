# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('proveedores.views',

    url(r"^$", "gestion_proveedor", name="gestion_proveedor"),
    url(r"^(?P<mod_id>\d+)/detalle$", "detalle_proveedor", name="detalle_proveedor"),
    url(r"^busca_proveedor$", "busca_proveedor", name="busca_proveedor"),

)
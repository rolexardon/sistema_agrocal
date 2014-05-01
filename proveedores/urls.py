# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('proveedores.views',

    url(r"^$", "gestion_proveedor", name="gestion_proveedor"),
    url(r"^(?P<mod_id>\d+)/detalle$", "detalle_proveedor", name="detalle_proveedor"),
    url(r"^busca_proveedor$", "busca_proveedor", name="busca_proveedor"),
<<<<<<< HEAD
    url(r"^ingreso_crear$", "ingreso_crear", name="ingreso_crear"),
=======
>>>>>>> 7c6f7ebb9828b38cdb02b715888e268a54ec46f6

)
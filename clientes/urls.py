# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('clientes.views',

    url(r"^$", "gestion_cliente", name="gestion_cliente"),
    url(r"^(?P<mod_id>\d+)/detalle$", "detalle_cliente", name="detalle_cliente"),
    url(r"^busca_cliente$", "busca_cliente", name="busca_cliente"),

)
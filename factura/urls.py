# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('factura.views',
    url(r"^ajax$", "get_ajax", name="get_ajax"),

    url(r"^$", "gestion_factura", name="gestion_factura"),
    url(r"^credito", "gestion_credito", name="gestion_credito"),
    url(r"^debito", "gestion_debito", name="gestion_debito"),

    url(r"^crear$", "factura_crear", name="factura_crear"),
    url(r"^crear/credito$", "credito_crear", name="credito_crear"),
    url(r"^crear/debito$", "debito_crear", name="debito_crear"),

    url(r"^(?P<mod_id>\d+)/detalle/factura$", "detalle_factura", name="detalle_factura"),
    url(r"^(?P<mod_id>\d+)/detalle/credito$", "detalle_credito", name="detalle_credito"),
    url(r"^(?P<mod_id>\d+)/detalle/debito$", "detalle_debito", name="detalle_debito"),

    url(r"^buscar$", "factura_buscar", name="factura_buscar"),
    url(r"^buscar/credito$", "credito_buscar", name="credito_buscar"),
    url(r"^buscar/debito$", "debito_buscar", name="debito_buscar"),
)# -*- coding: utf-8 -*-

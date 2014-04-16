# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('producto.views',

    url(r"^$", "gestion_producto", name="gestion_producto"),
    url(r"^(?P<mod_id>\d+)/detalle$", "detalle_producto", name="detalle_producto"),
    url(r"^busca_producto$", "busca_producto", name="busca_producto"),
    url(r"^promo", "gestion_promocion", name="gestion_promocion"),
    url(r"^(?P<mod_id>\d+)/detalle_promo$", "detalle_promocion", name="detalle_promocion"),
    url(r"^busca_promocion$", "busca_promocion", name="busca_promocion"),

)
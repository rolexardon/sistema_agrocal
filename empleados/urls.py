# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('empleados.views',

    url(r"^$", "gestion_empleado", name="gestion_empleado"),
    url(r"^crear$", "empleado_crear", name="empleado_crear"),
    url(r"^(?P<mod_id>\d+)/modificar$", "empleado_modificar", name="empleado_modificar"),
    url(r"^(?P<mod_id>\d+)/detalle$", "detalle_empleado", name="detalle_empleado"),
    url(r"^empleado_buscar$", "empleado_buscar", name="empleado_buscar"),
)
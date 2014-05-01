# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('principal.views',

    url(r"^$", "main", name="main"),

)
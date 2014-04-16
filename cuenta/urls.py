# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('cuenta.views',

    url(r'^account/login$','login_agrocal',name="login_agrocal"),
    url(r'^account/logout$','logout_agrocal',name="logout_agrocal"),

)
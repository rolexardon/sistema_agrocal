from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

admin.autodiscover()

import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sigps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^principal/', include('principal.urls')),
    url(r'^$', TemplateView.as_view(template_name='account_login.html'),  name='base'),
    url(r'^cuenta/', include('cuenta.urls')),
    url(r'^empleados/', include('empleados.urls')),
    url(r'^clientes/', include('clientes.urls')),
    url(r'^producto/', include('producto.urls')),
    url(r'^proveedores/', include('proveedores.urls')),
    url(r'^reportes/', include('reportes.urls')),
    url(r'^factura/', include('factura.urls')),

)
if settings.DEBUG:
        # static files (images, css, javascript, etc.)
        urlpatterns += patterns('',(r'^resources/(?P<path>.*)$',
                                    'django.views.static.serve',
                                    {'document_root': settings.MEDIA_ROOT}))

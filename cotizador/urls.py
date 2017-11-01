"""cotizador URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from residencial.views import domestico, get_name,start_page,prom_anual_kwhr,cotizacion_nPaneles,cotizacion_nPaneles2
#from residencial.modules import rutinas as rut
#rut.buildInvertersDict()
urlpatterns = [
    url(r'^$',start_page,name = 'start_page'),
    url(r'^admin/', admin.site.urls),
    url(r'^residencial/$', domestico, name = "domestico"),
    url(r'^get_name/$', get_name, name = "get_name"),
    url(r'^promedio_anual_kwhr/$', prom_anual_kwhr, name = "prom_anual_kwhr"),
    url(r'^promedio_anual_kwhr/cotizacion-residencial/(?P<nPaneles>[0-9]{5})$', cotizacion_nPaneles2, name = "cotizacion_nPaneles"),
    #url(r'^get_name/mensaje', get_name, name = "get_name"),
    #url(r'^your_name/', your_name, name = "your_name"),
]

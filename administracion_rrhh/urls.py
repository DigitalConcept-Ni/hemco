"""administracion_rrhh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from Aplicaciones.homepage.views import IndexView
from administracion_rrhh.views import dash

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('',IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('panelcentral/', include('Aplicaciones.RRHH.urls')),
    path('login/', include('Aplicaciones.login.urls')),
    path('Dashboard/', dash, name='dashboard'),
    path('query/', include('Aplicaciones.query.urls')),
    path('user/', include('Aplicaciones.user.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += static(settings.MEDIA_URL,  document_root = settings.MEDIA_ROOT)



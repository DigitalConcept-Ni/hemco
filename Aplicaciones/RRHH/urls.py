from django.urls import path

from Aplicaciones.RRHH.views.masivo.view import ExpedientesMasivo, ActualizacionMasiva
from Aplicaciones.RRHH.views.reporte.view import ReportExpedienteView, ReportMasivoView
from Aplicaciones.RRHH.views.secciones.view import *
from Aplicaciones.RRHH.views.documentos.view import *
from Aplicaciones.RRHH.views.expedientes.view import *
from Aplicaciones.RRHH.views.indexado.view import *

app_name = 'RRHH'

urlpatterns = [
    # urls Secciones
    path('secciones/list/', secciones_list, name='section_list'),
    path('secciones/add/', SeccionesCreateview.as_view(), name='section_add'),
    path('secciones/update/<int:pk>/', SeccionesUpdateiew.as_view(), name='section_update'),
    path('secciones/delete/<int:pk>/', SeccionesDeleteview.as_view(), name='section_delete'),
    # urls Documentos
    path('documentos/list/', DocumentoListView.as_view(), name='documento_list'),
    path('documentos/add/', DocumentoCreateView.as_view(), name='documento_add'),
    path('documentos/edit/<int:pk>/', DocumentoUpdateView.as_view(), name='documento_edit'),
    path('documentos/delete/<int:pk>/', DocumentoDeleteView.as_view(), name='documento_delete'),
    #urls Expedientes
    path('expedientes/list/', ExpedienteListview.as_view(), name='expediente_list'),
    path('expedientes/add/', ExpedienteCreateview.as_view(), name='expediente_add'),
    path('expedientes/edit/<int:pk>/', ExpedienteUpdateview.as_view(), name='expediente_edit'),
    path('expedientes/delete/<int:pk>/', ExpedienteDeleteview.as_view(), name='expediente_delete'),
    # urls Indexado
    path('Indexacion/list/', Indexlistview.as_view(), name='index_list'),
    path('Indexacion/add/', IndexCreateview.as_view(), name='index_add'),
    path('Indexacion/edit/<int:pk>/', IndexUpdateview.as_view(), name='index_edit'),
    path('Indexacion/delete/<int:pk>/', IndexDeleteview.as_view(), name='index_delete'),
    #PRUEBA DE MASIVO
    path('masivo/expedientes/', ExpedientesMasivo.as_view(), name = 'expedientes_masivo'),
    path('masivo/actualizacion/', ActualizacionMasiva.as_view(), name = 'actualizacion_masivo'),
    # path('masivo/', importar.as_view(), name = 'masivo_add'),

    # QUERY
    # path('query/', Queryview.as_view(), name = 'add_query'),

    # Reporte
    path('reporte/expediente/', ReportExpedienteView.as_view(), name = 'add_report'),
    path('reporte/documento/', ReportMasivoView.as_view(), name = 'add_report_masivo'),


]

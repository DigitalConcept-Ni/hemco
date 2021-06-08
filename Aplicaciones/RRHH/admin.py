from django.contrib import admin
from Aplicaciones.RRHH.models import *

# Register your models here.
admin.site.register(Secciones)
admin.site.register(Documentos)
admin.site.register(Registros)
admin.site.register(Expedientes)
admin.site.register(Indexaciones)


# @admin.register(Secciones)
# class section(admin.ModelAdmin):
#     list_display = ('id', 'nombre')
#     search_fields = ('nombre',)
#     ordering = ('-id',)

# @admin.register(Expedientes)
# class Expedientesadmin(admin.ModelAdmin):
#     list_display = ('cedula', 'primer_nombre', 'segundo_nombre', 'apellido_paterno',
#                     'apellido_materno', 'departamento', 'contrato', 'estado')
#     ordering = ('apellido_paterno',)
#     search_fields = ('cedula', 'primer_nombre', 'segundo_nombre', 'apellido_paterno',
#                      'apellido_materno', 'departamento', 'contrato')


# @admin.register(Registros)
# class registrosadmin(admin.ModelAdmin):
#     list_display = ('id', 'id_documento')
#     ordering = ('-id',)
#     search_fields = ('id', 'id_documento')


# @admin.register(Indexaciones)
# class indexacionsadmin(admin.ModelAdmin):
#     list_display = ('cedula', 'id_seccion', 'id_documento',
#                     'archivo', 'fecha_documento')
#     ordering = ('-cedula',)

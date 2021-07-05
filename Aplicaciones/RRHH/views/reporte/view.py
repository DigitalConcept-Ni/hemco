from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from Aplicaciones.RRHH.forms import MasivoForm, DocForm
from Aplicaciones.RRHH.models import Indexaciones, Documentos
from Aplicaciones.query.forms import query


class ReportExpedienteView(TemplateView):
    template_name = 'reporte/reporte.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'query_report':
                data = []
                docIndex = []
                docs = []
                print(request.POST)
                for d in Documentos.objects.all():
                    docs.append(str(d.nombre))
                #  dd = Es la variable que contiene los nombres de los documentos en indexaciones
                for dd in Indexaciones.objects.filter(cedula=request.POST['cedula']):
                    docIndex.append(str(dd.documento))
                    id = 0
                for ddocs in docs:
                    if ddocs in docIndex:
                        pass
                    else:
                        id += 1
                        data.append({'id': id, 'nombre': ddocs })
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
        # return render(request, 'dashboard.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reporte por expedientes'
        context['action'] = 'Expediente'
        context['form'] = query()
        context['entity'] = 'Reporte Expediente'
        return context

class ReportMasivoView(TemplateView):
    template_name = 'reporte/datatable.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'report_doc_masivo':
                data = []
                for i in Indexaciones.objects.all().order_by('cedula').distinct('cedula'):
                    if int(i.documento_id) == int(request.POST['documento']):
                        pass
                    else:
                        data.append({'id': i.cedula.get_cedula(), 'nombre': i.cedula.nombre_completo()})
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
        # return render(request, 'dashboard.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalle de documentos faltante por expedientes masivo'
        context['action'] = 'reporte_documento'
        context['formDoc'] = DocForm()
        context['entity'] = 'Reporte Masivo'
        return context


from django.db.models import Q
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, FormView

from Aplicaciones.RRHH.models import Expedientes, Indexaciones
from Aplicaciones.query.forms import query
from Aplicaciones.user.models import User


class Queryview(TemplateView):
    template_name = 'query/query.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            # print("cedula", cedula, 'sec:', seccion)
            # data = Expedientes.objects.get(pk=request.POST['Cedula']).toJSON()
            action = request.POST['action']
            if request.user.is_superuser:
                if action == 'query':
                    data = []
                    for i in Indexaciones.objects.all().filter(Q(cedula_id=request.POST['cedula']) & Q(seccion_id=request.POST['seccion'])):
                        data.append(i.toJSON())
            else:
                if action == 'query':
                    data = []
                    for u in User.objects.all().filter(id=request.user.id):
                        for i in Indexaciones.objects.all().filter(Q(cedula_id=request.POST['cedula']) & Q(documento_id = u.secccion)):
                            print(i)
                            data.append(i.toJSON())
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)


    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = 'Consulta de expedientes por seccion'
        data['action'] = 'query_expediente'
        data['entity'] = 'Consultas'
        data['form'] = query()
        return data

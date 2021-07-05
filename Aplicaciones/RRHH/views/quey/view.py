from django.core.serializers import json
from django.db.models import Q
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, FormView

from Aplicaciones.RRHH.forms import query
from Aplicaciones.RRHH.models import Expedientes, Indexaciones


class Queryview(FormView):
    template_name = 'query.html'
    form_class = query

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # form_class = self.get_form_class()
        # files = request.POST['Cedula']
        # data = {}
        try:
            result = request.POST
            print(result)
            data = []
            list = result.values()
            cont = 0
            for i in list:
                print(i)
                cont += 1
                if cont == 2:
                    cedula = i
                if cont == 4:
                    seccion = i
            print("cedula", cedula, 'sec:', seccion)
            # data = Expedientes.objects.get(pk=request.POST['Cedula']).toJSON()
            for n in Indexaciones.objects.filter(Q(cedula_id=cedula) & Q(seccion_id=seccion)):
                data.append(n.toJSON())
            print(data)
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = 'Consulta de Expedientes'
        # data['form'] = query()
        return data

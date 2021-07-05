from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView

from Aplicaciones.RRHH.forms import SeccionesForms
from Aplicaciones.RRHH.models import Secciones


def secciones_list(request):
    data = {
        'title': 'Listado de Secciones',
        'secciones': Secciones.objects.all()
    }
    return render(request, 'secciones/list.html', data)


class SeccionesCreateview(CreateView):
    model = Secciones
    form_class = SeccionesForms
    template_name = 'secciones/create.html'
    success_url = reverse_lazy('RRHH:section_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar Seccion'
        context['entity'] = 'Secciones'
        context['list_url'] = reverse_lazy('RRHH:expediente_list')
        context['action'] = 'add'
        return context

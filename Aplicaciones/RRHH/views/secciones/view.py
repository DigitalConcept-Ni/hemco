from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView

from Aplicaciones.RRHH.forms import SeccionesForms
from Aplicaciones.RRHH.models import Secciones


def secciones_list(request):
    data = {
        'title': 'Listado de Secciones',
        'secciones': Secciones.objects.all(),
        'create_url': reverse_lazy('RRHH:section_add')
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

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'No ha ingresado ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar Seccion'
        context['entity'] = 'Secciones'
        context['list_url'] = reverse_lazy('RRHH:section_list')
        context['action'] = 'add'
        return context

class SeccionesUpdateiew(UpdateView):
    model = Secciones
    form_class = SeccionesForms
    template_name = 'secciones/create.html'
    success_url = reverse_lazy('RRHH:section_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'No ha ingresado ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Modificar Seccion'
        context['entity'] = 'Secciones'
        context['list_url'] = reverse_lazy('RRHH:section_list')
        context['action'] = 'edit'
        return context

class SeccionesDeleteview(DeleteView):
    model = Secciones
    form_class = SeccionesForms
    template_name = 'secciones/delete.html'
    success_url = reverse_lazy('RRHH:section_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object =self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Seccion'
        context['entity'] = 'Secciones'
        context['list_url'] = reverse_lazy('RRHH:section_list')
        context['action'] = 'delete'
        return context


from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from Aplicaciones.RRHH.forms import ExpedienteForm
from Aplicaciones.RRHH.models import Expedientes


class ExpedienteListview(ListView):
    model = Expedientes
    template_name = 'expedientes/list.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Expedientes de Colaboradores'
        context['create_url'] = reverse_lazy('RRHH:expediente_add')
        context['entity'] = 'Expedientes'
        context['list_url'] = reverse_lazy('RRHH:expediente_list')
        return context


class ExpedienteCreateview(CreateView):
    model = Expedientes
    form_class = ExpedienteForm
    template_name = 'expedientes/create.html'
    success_url = reverse_lazy('RRHH:expediente_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar Colaborador'
        context['entity'] = 'Expedientes'
        context['list_url'] = reverse_lazy('RRHH:expediente_list')
        context['action'] = 'add'
        return context


class ExpedienteUpdateview(UpdateView):
    model = Expedientes
    form_class = ExpedienteForm
    template_name = 'expedientes/create.html'
    success_url = reverse_lazy('RRHH:expediente_list')

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return  super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Datos del Colaborador'
        context['entity'] = 'Expedientes'
        context['list_url'] = reverse_lazy('RRHH:expediente_list')
        context['action'] = 'edit'
        return context

class ExpedienteDeleteview(DeleteView):
    model = Expedientes
    form_class = ExpedienteForm
    template_name = 'expedientes/delete.html'
    success_url = reverse_lazy('RRHH:expediente_list')

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return  super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Expediente'
        context['entity'] = 'Expedientes'
        context['list_url'] = reverse_lazy('RRHH:expediente_list')
        return context
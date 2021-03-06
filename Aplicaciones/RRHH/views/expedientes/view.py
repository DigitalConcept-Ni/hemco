from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from Aplicaciones.RRHH.forms import ExpedienteForm
from Aplicaciones.RRHH.mixin import IsSuperUserMixin
from Aplicaciones.RRHH.models import Expedientes


class ExpedienteListview(LoginRequiredMixin,IsSuperUserMixin, ListView):
    model = Expedientes
    template_name = 'expedientes/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        pass


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
        context['title'] = 'Actualizar expediente'
        context['entity'] = 'Expedientes'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context

class ExpedienteUpdateview(UpdateView):
    model = Expedientes
    form_class = ExpedienteForm
    template_name = 'expedientes/create.html'
    success_url = reverse_lazy('RRHH:expediente_list')

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
        context['title'] = 'Modificar expediente'
        context['entity'] = 'Expedientes'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context

class ExpedienteDeleteview(DeleteView):
    model = Expedientes
    form_class = ExpedienteForm
    template_name = 'expedientes/delete.html'
    success_url = reverse_lazy('RRHH:expediente_list')

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
        context['title'] = 'Eliminar expediente'
        context['entity'] = 'Expedientes'
        context['list_url'] = self.success_url
        context['action'] = 'delete'
        return context
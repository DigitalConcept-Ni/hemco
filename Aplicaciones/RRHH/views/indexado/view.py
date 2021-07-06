from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from Aplicaciones.RRHH.forms import IndexadoForms
from Aplicaciones.RRHH.models import Indexaciones


class Indexlistview(ListView):
    model = Indexaciones
    template_name = 'indexado/list.html'

    # def get_queryset(self):
    #     return Documentos.objects.filter(sombre__startswith='l')
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista de expedientes completos'
        context['create_url'] = reverse_lazy('RRHH:index_add')
        context['entity'] = 'Indexado'
        context['list_url'] = reverse_lazy('RRHH:index_list')
        return context

class IndexCreateview(CreateView):
    model = Indexaciones
    form_class = IndexadoForms
    template_name = 'indexado/create.html'
    success_url = reverse_lazy('RRHH:index_list')

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
        context['entity'] = 'Indexaciones'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context

class IndexUpdateview(UpdateView):
    model = Indexaciones
    form_class = IndexadoForms
    template_name = 'indexado/create.html'
    success_url = reverse_lazy('RRHH:index_list')

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
        context['title'] = 'Modificar Indexacion'
        context['entity'] = 'Indexaciones'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context

class IndexDeleteview(DeleteView):
    model = Indexaciones
    form_class = IndexadoForms
    template_name = 'indexado/delete.html'
    success_url = reverse_lazy('RRHH:index_list')

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
        context['title'] = 'Eliminar Indexacion'
        context['entity'] = 'indexaciones'
        context['list_url'] = self.success_url
        context['action'] = 'delete'
        return context
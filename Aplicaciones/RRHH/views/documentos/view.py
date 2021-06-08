from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from Aplicaciones.RRHH.forms import DocumentosForms
from Aplicaciones.RRHH.models import Documentos


class DocumentoListView(ListView):
    model = Documentos
    template_name = 'documentos/list.html'

    # def get_queryset(self):
    #     return Documentos.objects.filter(sombre__startswith='l')
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Documentos'
        context['create_url'] = reverse_lazy('RRHH:documento_add')
        context['entity'] = 'Documentos'
        context['list_url'] = reverse_lazy('RRHH:documento_list')
        return context

    # def post(self, request, *args, **kwargs):
    #     data = {'nombre': 'Bryan', 'apellido': 'Urbina'}
    #     return JsonResponse(data)


class DocumentoCreateView(CreateView):
    model = Documentos
    form_class = DocumentosForms
    template_name = 'documentos/create.html'
    success_url = reverse_lazy('RRHH:documento_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creacion de Documentos'
        context['entity'] = 'Documentos'
        context['list_url'] = reverse_lazy('RRHH:documento_list')
        context['action'] = 'add'
        return context


class DocumentoUpdateView(UpdateView):
    model = Documentos
    form_class = DocumentosForms
    template_name = 'documentos/create.html'
    success_url = reverse_lazy('RRHH:documento_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar nombre del Documento'
        context['entity'] = 'Documentos'
        context['list_url'] = reverse_lazy('RRHH:documento_list')
        context['action'] = 'edit'
        return context


class DocumentoDeleteView(DeleteView):
    model = Documentos
    form_class = DocumentosForms
    template_name = 'documentos/delete.html'
    success_url = reverse_lazy('RRHH:documento_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Documento'
        context['entity'] = 'Documentos'
        context['list_url'] = reverse_lazy('RRHH:documento_list')
        return context

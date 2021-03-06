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

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = []
            print(request.POST)
            action = request.POST['action']
            if action == 'search_data':
                for d in Documentos.objects.all():
                    data.append(d.toJSON())
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Documentos'
        context['create_url'] = reverse_lazy('RRHH:documento_add')
        context['entity'] = 'Documentos'
        context['list_url'] = reverse_lazy('RRHH:documento_list')
        return context

class DocumentoCreateView(CreateView):
    model = Documentos
    form_class = DocumentosForms
    template_name = 'documentos/create.html'
    success_url = reverse_lazy('RRHH:documento_list')

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
        context['title'] = 'Actualizar documento'
        context['entity'] = 'Documentos'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context

class DocumentoUpdateView(UpdateView):
    model = Documentos
    form_class = DocumentosForms
    template_name = 'documentos/create.html'
    success_url = reverse_lazy('RRHH:documento_list')

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
        context['title'] = 'Modificar documento'
        context['entity'] = 'Documentos'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context

class DocumentoDeleteView(DeleteView):
    model = Documentos
    form_class = DocumentosForms
    template_name = 'documentos/delete.html'
    success_url = reverse_lazy('RRHH:documento_list')

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
        context['title'] = 'Eliminar documento'
        context['entity'] = 'Documentos'
        context['list_url'] = self.success_url
        context['action'] = 'delete'
        return context

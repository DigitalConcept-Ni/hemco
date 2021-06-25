from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView
from tablib import Dataset

from Aplicaciones.RRHH.forms import FileFieldForm
from Aplicaciones.RRHH.resources import ExpedientesResource


class ExpedientesMasivo(FormView):
    form_class = FileFieldForm
    template_name = 'masivo/upload.html'
    success_url = reverse_lazy('RRHH:index_list')

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('pdf')
        prueba = request.POST['action']
        print(prueba)
        print(files)

        dd = []
        if form.is_valid():
            for f in files:
                dd.extend([f])
        print('archivos: ', len(dd))
        persona_resource = ExpedientesResource()
        dataset = Dataset()
        print(dataset)
        nuevas_personas = request.FILES['xlsfile']
        print(nuevas_personas)
        imported_data = dataset.load(nuevas_personas.read())
        print(dataset)
        dataset.append_col(dd, header='archivo')
        print(dataset)
        # result = persona_resource.import_data(dataset, dry_run=True)  # Test the data import
        # print('problemas: ',result.has_errors())
        # if not result.has_errors():
        #     persona_resource.import_data(dataset, dry_run=False)  # Actually import now
        return render(request, 'expedientes/list.html')

        #     return self.form_valid(form)
        # else:
        #     return self.form_invalid(form)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'expedientes'
        context['action'] = 'Exp'
        return context



class ActualizacionMasiva(FormView):
    # template = loader.get_template('export/importar.html')

    form_class = FileFieldForm
    template_name = 'masivo/upload.html'
    success_url = reverse_lazy('RRHH:index_list')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('pdf')
        dd = []

        if form.is_valid():
            for f in files:
                dd.extend([f])
        print('archivos: ', len(dd))
        persona_resource = SeccionResource()
        dataset = Dataset()
        # print(dataset)
        nuevas_personas = request.FILES['xlsfile']
        print(nuevas_personas)
        imported_data = dataset.load(nuevas_personas.read())
        print(dataset)
        dataset.append_col(dd, header='archivo')
        print(dataset)
        # result = persona_resource.import_data(dataset, dry_run=True)  # Test the data import
        # print('problemas: ', result.has_errors())
        # if not result.has_errors():
        #     persona_resource.import_data(dataset, dry_run=False)  # Actually import now
        # return render(request, 'expedientes/list.html')

        #     return self.form_valid(form)
        # else:
        #     return self.form_invalid(form)
"""    if FormView.method == 'POST':
        persona_resource = SeccionResource()
        dataset = Dataset()
        # print(dataset)
        nuevas_personas = FormView.FILES['xlsfile']
        # print(nuevas_personas)
        imported_data = dataset.load(nuevas_personas.read())
        # print(dataset)
        result = persona_resource.import_data(dataset, dry_run=True)  # Test the data import
        print('problemas: ',result.has_errors())
        if not result.has_errors():
            persona_resource.import_data(dataset, dry_run=False)  # Actually import now
    return render(FormView, 'masivo/upload.html')"""

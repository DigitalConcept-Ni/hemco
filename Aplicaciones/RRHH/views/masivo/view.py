from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView, TemplateView
from tablib import Dataset

from Aplicaciones.RRHH.forms import FileFieldForm, MasivoForm
from Aplicaciones.RRHH.models import Expedientes, Secciones, Documentos
from Aplicaciones.RRHH.resources import ExpedientesResource, ActualizacionResource


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
        result = persona_resource.import_data(dataset, dry_run=True)  # Test the data import
        print('problemas: ', result.has_errors())
        if not result.has_errors():
            persona_resource.import_data(dataset, dry_run=False)  # Actually import now
            return render(request, 'expedientes/list.html')

        #     return self.form_valid(form)
        # else:
        #     return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ingreso masivo de expedientes'
        context['action'] = 'expedientes'
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
        print(request.POST)
        data = {}
        # Apartado de la seleccion de las secciones y que documentos tiene
        try:
            action = request.POST['action']
            if action == 'search_section_id':
                data = [{'id': '', 'text': '----------'}]
                for i in Documentos.objects.filter(seccion_id=request.POST['id']):
                    data.append({'id': i.id,  'text': i.nombre})
                return JsonResponse(data, safe=False)
            else:
                data['error'] = 'Ha ocurrido un error'
            # Apartado de la subida del archivo excel
            if action == 'actualizacion':
                if form.is_valid():
                    cedula = []
                    seccion = []
                    documento = []
                    archivosPDF = []
                    for f in files:
                        archivosPDF.extend([f])
                    print('archivos: ', len(archivosPDF))
                    persona_resource = ActualizacionResource()
                    dataset = Dataset()
                    # print(dataset)
                    nuevas_personas = request.FILES['xlsfile']
                    print(nuevas_personas)
                    imported_data = dataset.load(nuevas_personas.read())
                    for c in dataset['cedula']:
                        for m in Expedientes.objects.filter(cedula=c):
                            cedula.append(m.get_id())
                    for r in range(len(dataset['cedula'])):
                        seccion.append(request.POST['Secciones'])
                        documento.append(request.POST['Documentos'])
                    del dataset['cedula']
                    dataset.insert_col(1, cedula, header='cedula')
                    dataset.insert_col(2, seccion, header='seccion')
                    dataset.insert_col(3, documento, header='documento')
                    dataset.append_col(archivosPDF, header='archivo')
                    # print(dataset)
                    result = persona_resource.import_data(dataset, dry_run=True)  # Test the data import
                    print('problemas: ', result.has_errors())
                    if not result.has_errors():
                        persona_resource.import_data(dataset, dry_run=False)  # Actually import now
                        return render(request, 'dashboard.html')
        except Exception as e:
            data['error'] = str(e)
        return render(request, 'dashboard.html')


        #     return self.form_valid(form)
        # else:
        #     return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizacion Masiva'
        context['action'] = 'actualizacion'
        context['mForm'] = MasivoForm()
        return context

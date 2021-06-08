from django.shortcuts import render
from Aplicaciones.RRHH.models import Secciones


def secciones_list(request):
    data = {
        'title': 'Listado de Secciones',
        'secciones': Secciones.objects.all()
    }
    return render(request, 'secciones/list.html', data)
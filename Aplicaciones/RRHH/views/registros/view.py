from django.shortcuts import render
from Aplicaciones.RRHH.models import Registros


def registro_list(request):
    data = {
        'title': 'lista de Registros',
        'registros': Registros.objects.all()
    }
    return render(request, 'registros/list.html', data)
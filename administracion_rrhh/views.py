#Request = Solicitud, pedido
#Response = Respuesta

from django.http import HttpResponse
from django.template import Context, Template, loader
from django.template.loader import get_template
import datetime
from django.shortcuts import render

def dash(request):
    return render(request, 'dashboard.html', {})

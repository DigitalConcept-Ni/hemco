from django.forms import *

from Aplicaciones.RRHH.models import Expedientes, Secciones


class query(Form):
    Cedula = ModelChoiceField(queryset=Expedientes.objects.all(), widget=Select(
        attrs={'class': 'form-control'}))
    Secciones = ModelChoiceField(queryset=Secciones.objects.all(), widget=Select(
        attrs={'class': 'form-control'}))

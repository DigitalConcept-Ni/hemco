from django.forms import *
from django import forms
from Aplicaciones.RRHH.models import Documentos, Indexaciones, Expedientes, Secciones


class DocumentosForms(ModelForm):
    class Meta:
        model = Documentos
        fields = '__all__'
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese el nombre de un documento',
                    'autofocus': True
                })
        }


class IndexadoForms(ModelForm):
    class Meta:
        model = Indexaciones
        fields = '__all__'

        widgets = {
            'fecha_documento': DateInput(
                attrs={
                    'type': 'date',
                }
            ),
            # 'archivo': ClearableFileInput(attrs ={
            #     'multiple': True
            # })
        }


class ExpedienteForm(ModelForm):
    class Meta:
        model = Expedientes
        fields = '__all__'
        widgets = {
            'cedula': TextInput(
                attrs={
                    'autofocus': True
                })
        }


class FileFieldForm(forms.Form):
    pdf = forms.FileField(widget=forms.ClearableFileInput(
        attrs={'multiple': True,
               'class': 'form-control',
               }))

    # file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


class query(Form):
    Cedula = ModelChoiceField(queryset=Expedientes.objects.all(), widget=Select(
        attrs={'class': 'form-control'}))
    Secciones = ModelChoiceField(queryset=Secciones.objects.all(), widget=Select(
        attrs={'class': 'form-control'}))


class MasivoForm(Form):
    Secciones = ModelChoiceField(queryset=Secciones.objects.all(), widget=Select(
        attrs={'class': 'form-control select2'}))
    Documentos = ModelChoiceField(queryset=Documentos.objects.none(), widget=Select(
        attrs={'class': 'form-control select2'}))

from django.forms import *
from django import forms
from Aplicaciones.RRHH.models import Documentos, Indexaciones, Expedientes


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


# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Indexaciones
#         exclude = [id, ]
#
#     def clean(self):
#         archivo = self.cleaned_data.get('archivo')
#         if archivo == None:
#             raise forms.ValidationError("Product offer price cannot be greater than Product MRP.")
#         return self.cleaned_data


class FileFieldForm(forms.Form):

    pdf = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    #file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
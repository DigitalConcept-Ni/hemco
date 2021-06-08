from django.db import models


# Create your models here.

class doc(models.Model):
    nombre = models.CharField(max_length=12)
    archivo = models.FileField(upload_to='pdf/%Y/%m/%d', null=True, blank=True)


class Secciones(models.Model):
    nombre = models.CharField(max_length=12)
    tipo_documento = models.CharField(max_length=30)

    def __str__(self):
        return '{0}'.format(self.nombre)


class Documentos(models.Model):
    nombre = models.CharField(max_length=40, verbose_name='Nombre Documento', unique=True)

    def __str__(self):
        return '{0}'.format(self.nombre)


class Registros(models.Model):
    seccion = models.ForeignKey(
        Secciones, on_delete=models.CASCADE)
    documento = models.ForeignKey(
        Documentos, on_delete=models.CASCADE)

    def __str__(self):
        return '{0} {1}'.format(self.seccion, self.documento)


class Expedientes(models.Model):
    cedula = models.CharField(max_length=14)
    primer_nombre = models.CharField(max_length=35)
    segundo_nombre = models.CharField(max_length=35)
    apellido_paterno = models.CharField(max_length=35)
    apellido_materno = models.CharField(max_length=35)
    departamento = models.CharField(max_length=30)
    lista_contrato = [('D', 'DETERMINADO'),
                      ('I', 'INDETERMINADO')]
    contrato = models.CharField(
        max_length=1, choices=lista_contrato, default='D')
    lista_estado = [('A', 'ACTIVO'),
                    ('I', 'INACTIVO')]
    estado = models.CharField(max_length=1, choices=lista_estado, default='A')
    archivo = models.FileField(upload_to='pdf/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return '{0} {1} {2} {3}'.format(self.primer_nombre, self.segundo_nombre, self.apellido_paterno,
                                        self.apellido_materno)


class Indexaciones(models.Model):
    cedula = models.ForeignKey(
        Expedientes, on_delete=models.CASCADE)
    seccion = models.ForeignKey(
        Secciones, on_delete=models.CASCADE)
    documento = models.ForeignKey(
        Documentos, on_delete=models.CASCADE)
    fecha_documento = models.DateField(null=True, blank=True)
    archivo = models.FileField(upload_to='pdf/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return '{0} - {1} -  {2} - {3}'.format(self.cedula, self.seccion, self.documento, self.archivo)

    def get_fecha(self):
        if self.fecha_documento:
            return '{}'.format(self.fecha_documento)
        return '{}'.format('No requerido')

from import_export import resources

from Aplicaciones.RRHH.models import Indexaciones, Expedientes


class ExpedientesResource(resources.ModelResource):

    # def before_import(self, dataset, using_transactions, dry_run, **kwargs):
    #     ll = ['en', 'cristo', 'que me fortalece']
    #     dataset.append_col(dd, header='archivo')
    #     print(**kwargs)

    class Meta:
        model = Expedientes
        # fields = '__all__'

class ActualizacionResource(resources.ModelResource):

    # def before_import(self, dataset, using_transactions, dry_run, **kwargs):
    #     ll = ['en', 'cristo', 'que me fortalece']
    #     dataset.append_col(dd, header='archivo')
    #     print(**kwargs)

    class Meta:
        model = Indexaciones
        # fields = '__all__'
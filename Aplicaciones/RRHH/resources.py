from import_export import resources

from Aplicaciones.RRHH.models import Secciones, Indexaciones, doc, Expedientes


class SeccionResource(resources.ModelResource):

    # def before_import(self, dataset, using_transactions, dry_run, **kwargs):
    #     ll = ['en', 'cristo', 'que me fortalece']
    #     dataset.append_col(dd, header='archivo')
    #     print(**kwargs)

    class Meta:
        model = Expedientes
        # fields = '__all__'

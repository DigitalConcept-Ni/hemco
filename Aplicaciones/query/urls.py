from django.urls import path

from Aplicaciones.query.views import Queryview
app_name = 'query'

urlpatterns = [
    # QUERY
    path('expedientes/', Queryview.as_view(), name = 'add_query'),

]
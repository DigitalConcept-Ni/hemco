from django.urls import path

from Aplicaciones.login.views import *

urlpatterns = [
    path('', LoginFormview.as_view(), name='login'),
    path('out/', LogoutFormview.as_view(), name='logout'),
]

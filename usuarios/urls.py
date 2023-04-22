from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('cadastro', cadastro, name='cadastro'),
    path('login/', login, name='login'),
    path('pag1', pagina1, name='pag1'),
    path('pag2', pagina2, name='pag2'),
]
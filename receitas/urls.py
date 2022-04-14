
from django.contrib import admin
from django.urls import path

from .views import busca,receita, cria_receita, deleta_receita, edita_receita, atualiza_receita, index

urlpatterns = [
    path('', index, name='index'),
    path('<int:receita_id>', receita, name='receita'),
    path('buscar', busca, name='buscar'),
    path('cria/receita', cria_receita, name='criar_receita'),
    path('deleta/<int:receita_id>',deleta_receita, name='deleta_receita'),
    path('edita/<int:receita_id>',edita_receita, name='editar_receita'),
    path('atualiza_receita', atualiza_receita, name='atualizar_receita')
]


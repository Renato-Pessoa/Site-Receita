from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout,name='logout'),
    path('cria/receita', views.criaReceita, name='cria_receita'),
    path('deleta_receita/<int:receita_id>', views.deletaReceita, name='deleta_receita'),
    path('edita_receita/<int:receita_id>', views.editaReceita, name='edita_receita'),
]
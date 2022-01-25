from django.contrib import admin
from .models import Receita

class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'categoria', 'publicada')  # Mostrando o id, o nome da receita e a categoria no admin ao invés de 'Receitas.object'
    list_display_links = ('id', 'nome_receita', 'categoria')  # Transformando id e nome da receita em links.
    search_fields = ('nome_receita',)  # Adicionando um campo de busca por nome de receita no admin.
    list_filter = ('categoria',)  # Adicionando filtro de categoria
    list_editable = ('publicada',)  # Adiciona uma caixa para ficar mais fácil de marcar/desmarcar a opção de publicada.
    list_per_page = 10  # Adicionando um limite de receita por página.


admin.site.register(Receita, ListandoReceitas)  # Registrado as receitas e seus conteúdos. 

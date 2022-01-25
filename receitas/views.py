from django.shortcuts import get_object_or_404, render
from .models import Receita

def index(request):

    receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)  # Está buscando itens filtrados que estão marcados com a aba de publicados e ordenados por data mais recente.

    dados = {
        'receitas' : receitas
    }
    return render(request, "index.html", dados)  

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    receita_a_exibir = {
        'receita' : receita
    }

    return render(request,'receita.html', receita_a_exibir)


def buscar(request):
    lista_receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)  # Recebendo todas as receitas publicadas no site

    if 'buscar' in request.GET:  # Se o input buscar for True   
        nome_a_buscar = request.GET['buscar']  # Atribuindo o nome pesquisado 
        if buscar:  # Caso a função seja verdadeira
            lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)  

    dados = {
        'receitas': lista_receitas
    }

    return render(request, 'buscar.html', dados)
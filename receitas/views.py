from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Receita

# Create your views here.


def index(request):
    # receita = Receita.objects.all()
    receita = Receita.objects.order_by("date_receita").filter(publicado=True)

    dados = {"receitas": receita}

    return render(request, 'index.html', dados)


def receita(request, id_receita):
    detalhes_receita = get_object_or_404(Receita, pk=id_receita)

    dados = {
        "receita": detalhes_receita
    }

    return render(request, 'receita.html', dados)


def http_request(request):
    return HttpResponse("<h1><h1>")

def buscar(request):

    # todas as receitas
    lista_receitas = Receita.objects.order_by("date_receita").filter(publicado=True)

    # verifica se nos parâmetros passados na url existe o queryParam buscar
    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']

        if buscar:
            # filtra as receitas pelo texto contido
            lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)

    dados = {
        "receitas" : lista_receitas
    }

    return render(request, 'buscar.html', dados)
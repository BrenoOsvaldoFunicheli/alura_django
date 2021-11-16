from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Receita

# Create your views here.


def index(request):
    receita = Receita.objects.all()

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

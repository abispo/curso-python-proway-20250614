from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Pergunta

def index(request):
    ultimas_cinco_perguntas = Pergunta.objects.order_by("-data_publicacao")[:5]
    contexto = {"ultimas_cinco_perguntas": ultimas_cinco_perguntas}

    return render(request, "enquetes/index.html", contexto)


def detalhes(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)

    return render(
        request,
        "enquetes/detalhes.html",
        context={"pergunta": pergunta}
    )


def resultados(request, pergunta_id):
    return HttpResponse(
        f"Você está na página de resultados da pergunta '{pergunta_id}'."
    )


def votar(request, pergunta_id):
    return HttpResponse(f"Você está votando em uma opção da pergunta '{pergunta_id}'.")

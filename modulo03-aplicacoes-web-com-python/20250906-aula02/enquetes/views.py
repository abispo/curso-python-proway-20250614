from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Pergunta, Opcao

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
    
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)

    try:
        opcao_selecionada = pergunta.opcao_set.get(pk=request.POST["opcao"])
    except (KeyError, Opcao.DoesNotExist):
        return render(
            request,
            "enquetes/detalhes.html",
            {
                "pergunta": pergunta,
                "mensagem_erro": "Você deve selecionar uma opção"
            }
        )
    
    else:
        opcao_selecionada.votos = F("votos") + 1
        opcao_selecionada.save()

        return HttpResponseRedirect(
            reverse("enquetes:resultados", args=(pergunta.id,))
        )

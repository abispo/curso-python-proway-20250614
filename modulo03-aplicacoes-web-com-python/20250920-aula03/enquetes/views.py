from django.db.models import F, Avg
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Pergunta, Opcao, FeedbackPergunta

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
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
    media_feedback = pergunta.feedbackpergunta_set.aggregate(media=Avg("nota"))

    return render(
        request,
        "enquetes/resultados.html",
        {"pergunta": pergunta, "media_feedback": media_feedback["media"]}
    )


def votar(request, pergunta_id):
    
    # A função get_object_or_404 retorna a instância do objeto se existir, se não, lança o erro 404
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)

    try:
        # Na linha abaixo vamos tentar carregar a opção a partir do valor que está armazenado no atributo POST do objeto request. Caso não exista a chave opcao, ou essa opcao não exista na tabela, será gerada uma exceção
        opcao_selecionada = pergunta.opcao_set.get(pk=request.POST["opcao"])
    except (KeyError, Opcao.DoesNotExist):
        # O template é novamente renderizado, porém com uma mensagem de erro na tela.
        return render(
            request,
            "enquetes/detalhes.html",
            {
                "pergunta": pergunta,
                "mensagem_erro": "Você deve selecionar uma opção"
            }
        )
    
    else:
        # Abaixo incrementamos o valor do atributo votos da opcao em 1, e depois salvamos os dados na tabela
        opcao_selecionada.votos = F("votos") + 1
        opcao_selecionada.save()

        # Após receber uma requisição do tipo POST, temos que utilizar o redirect para redicionar o usuário para outra página. A função reverse vai gerar a URL de acordo com o namespace e o nome, enquando o parâmetro args é utilizado quando a rota possui algum parâmetro.
        return HttpResponseRedirect(
            reverse("enquetes:resultados", args=(pergunta.id,))
        )

def feedback_pergunta(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)

    try:
        nota = request.POST["nota"]

    except KeyError:
        return HttpResponseRedirect(
            reverse("enquetes:resultados", args=(pergunta.id,))
        )

    feedback_pergunta = FeedbackPergunta(nota=int(nota), pergunta=pergunta)
    feedback_pergunta.save()
    
    return HttpResponseRedirect(
        reverse("enquetes:resultados", args=(pergunta.id,))
    )
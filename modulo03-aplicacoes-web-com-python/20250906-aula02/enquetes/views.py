from django.http import HttpResponse

from .models import Pergunta

def index(request):
    ultimas_cinco_perguntas = Pergunta.objects.order_by("-data_publicacao")[:5]
    saida = ", ".join([pergunta.texto_pergunta for pergunta in ultimas_cinco_perguntas])

    return HttpResponse(saida)


def detalhes(request, pergunta_id):
    return HttpResponse(f"Você está na página de detalhes da pergunta '{pergunta_id}'.")


def resultados(request, pergunta_id):
    return HttpResponse(
        f"Você está na página de resultados da pergunta '{pergunta_id}'."
    )


def votar(request, pergunta_id):
    return HttpResponse(f"Você está votando em uma opção da pergunta '{pergunta_id}'.")

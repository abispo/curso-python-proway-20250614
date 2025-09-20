from django.db.models import Count, Avg
from django.shortcuts import render

from enquetes.models import Pergunta, Opcao

def index(request):

    # O método count equivale ao comando sql SELECT COUNT(id) FROM perguntas
    qtd_perguntas_cadastradas = Pergunta.objects.count()

    # Outra maneira de contar a quantidade de registros
    qtd_opcoes_cadastradas = len(Opcao.objects.all())

    # Maneira simples de calcular a média de opções por pergunta
    media_opcoes_pergunta = qtd_opcoes_cadastradas / qtd_perguntas_cadastradas

    # O método annotate serve para criarmos atributos em tempo de execução para os objetos retornados na consulta. Ou seja, um objeto do tipo Pergunta terá além de id, texto e data_publicacao, o atributo numero_de_opcoes.
    # Além disso, utilizamos o método aggregate para retornar a média de opções por pergunta, utilizando a classe Avg no atributo numero_de_opcoes que foi criado para cada objeto Pergunta da consulta
    # Como o método aggregate retorna um dicionário, pegamos no final o valor associado a chave 'media_opcoes'
    # valor_annotate = Pergunta.objects.annotate(
    #     numero_de_opcoes=Count("opcao")
    # )
    # valor_aggregate = valor_annotate.aggregate(media_opcoes=Avg("numero_de_opcoes"))
    # media_opcoes_pergunta = valor_aggregate["media_opcoes"]

    return render(
        request,
        template_name="estatisticas/index.html",
        context={
            "qtd_perguntas_cadastradas": qtd_perguntas_cadastradas,
            "qtd_opcoes_cadastradas": qtd_opcoes_cadastradas,
            "media_opcoes_pergunta": media_opcoes_pergunta
        }
    )
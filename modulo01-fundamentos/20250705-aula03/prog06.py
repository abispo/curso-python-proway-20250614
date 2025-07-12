"""
Funções (Procedures)

Função Lambda

As funções lambda também são conhecidas como funções anônimas, ou seja, funções que não possuem um nome e que são utilizadas geralmente em casos específicos. No Python, geralmente criamos essas funções para serem passadas como parâmetros de uma outra função.
"""

from typing import Dict


def liberar_acesso(usuario: Dict[str, int]) -> bool:
    return usuario.get("score", 0) >= 8

if __name__ == "__main__":
    usuarios = [
        {"nome": "Maria", "score": 6},
        {"nome": "Marcela", "score": 9},
        {"nome": "Rita", "score": 8},
        {"nome": "Barbara", "score": 10},
        {"nome": "Carla", "score": 5}
    ]

    # usuarios_liberados = []
    # for usuario in usuarios:
    #     if liberar_acesso(usuario.get("score")):
    #         usuarios_liberados.append(usuario)

    # Filtrando os usuarios com score maior ou igual a 8
    usuarios_liberados = list(filter(liberar_acesso, usuarios))
    print(usuarios_liberados)

    # Utilizando uma função anônima (lambda)
    usuarios_lambda = list(filter(lambda x: x.get("score") < 8, usuarios))
    print(usuarios_lambda)

    # Para cada item da lista usuarios, a função filter irá executar a função lambda (anônima). Caso o valor de retorno da função executada seja True, esse valor da lista será retornado no iterável do filter.
"""
Estruturas de repetição no Python

laço while

De maneira semelhante ao laço for, utilizamos o laço while quando queremos executar um determinado bloco de código de maneira repetida. A diferença do while pro for é que a condição de parada é determinada por nós, ou seja, enquanto uma condição tal for verdadeira.
"""

from random import randint
from time import sleep

if __name__ == "__main__":

    """
    No exemplo abaixo iremos utilizar o laço while e o tipo de dado dicionário para simular uma batalha entre 2 personagens.

    Dicionários são estruturas de dados que possuem o formato chave: valor. Geralmente as chaves são do tipo string, enquanto os valores podem ser de qualquer tipo, inclusive outros dicionários. Diferente dos valores, podemos ter como chaves apenas os seguintes tipos: strings, numeros e valores booleanos. Dicionários são iteráveis, mutáveis e não permitem chaves duplicadas.
    """

    # Vamos criar 2 dicionários, 1 para cada personagem. Assim como listas, podemos criar um dicionário de 2 maneiras:

    heroi = {
        "nome": "Aragorn",
        "ataque": 15,
        "defesa": 10,
        "hp": 20
    }

    monstro = dict(
        nome="Uruk-Hai",
        ataque=13,
        defesa=12,
        hp=25
    )

    existe_vencedor = False
    vencedor = None

    while not existe_vencedor:
        
        for numero in range(2, 4):
            if numero % 2 == 0:
                atacante = heroi
                defensor = monstro

            else:
                atacante = monstro
                defensor = heroi

            print(f"{atacante['nome']} ataca {defensor['nome']}!")
            dado_ataque = randint(1, 6)
            dado_defesa = randint(1, 6)

            ataque_atacante = atacante.get("ataque") + dado_ataque
            defesa_defensor = defensor.get("defesa") + dado_defesa

            sleep(1)

            if ataque_atacante > defesa_defensor:
                print(f"{atacante['nome']} acertou um golpe no {defensor['nome']}!")
                defesa_defensor["hp"] = defesa_defensor["hp"] - (ataque_atacante - defensor["defesa"])

            else:
                print(f"{defensor['nome']} defendeu o ataque de {atacante['nome']}!")

            sleep(1)

            if defensor["hp"] <= 0:
                existe_vencedor = True
                vencedor = atacante
                break

    print(f"Vencedor: {vencedor['nome']}!")
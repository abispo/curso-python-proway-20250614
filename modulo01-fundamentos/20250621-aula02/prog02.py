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
        hp=1
    )

    existe_vencedor = False
    vencedor = None

    # Enquanto a condição que colocamos no laço while for True, o bloco será executado. Temos que tomar cuidado para garantir que o bloco de código possua alguma instrução que possibilite a condição do loop ser False, ou então corremos o risco de executar um loop infinito.
    while not existe_vencedor:

        # Assim como o laço for, no laço while também podemos utilizar as instruções break e continue, que se comportarão exatamente como no laço for. Assim como também podemos utilizar o bloco else
        
        for numero in range(2, 4):
            if numero % 2 == 0:
                atacante = heroi
                defensor = monstro

            else:
                atacante = monstro
                defensor = heroi

            # Podemos acessar o valor associado a uma chave do dicionários de 2 maneiras: Diretamente utilizando a sintaxe de colchetes, onde passamos o nome da chave
            print(f"{atacante['nome']} ataca {defensor['nome']}!")
            dado_ataque = randint(1, 6)
            dado_defesa = randint(1, 6)

            # Utilizando essa sintaxe, a chave indicada deve existir. Caso não exista, a exceção KeyError é lançada.

            # Podemos também utilizar o método get. Esse método é mais seguro do que o método de colchetes, pois caso a chave não exista no dicionário, será retornado o valor None, ou o valor padrão que definirmos como segundo parâmetro desse método
            ataque_atacante = atacante.get("ataque") + dado_ataque
            defesa_defensor = defensor.get("defesa") + dado_defesa

            # A função sleep faz o programa "esperar" a quantidade de segundos informada na chamada
            sleep(1)

            if ataque_atacante > defesa_defensor:
                print(f"{atacante['nome']} acertou um golpe no {defensor['nome']}!")

                # Assim como listas, dicionários são mutáveis, ou seja, podemos alterar diretamente um valor informado a chave associada a esse valor. Caso essa chave não exista no dicionário, ela será criada.
                defensor["hp"] = defensor["hp"] - (ataque_atacante - defensor["defesa"])

            else:
                print(f"{defensor['nome']} defendeu o ataque de {atacante['nome']}!")

            sleep(1)

            print("*"*20)
            print(f"{atacante['nome']} HP: {atacante['hp']}.")
            print(f"{defensor['nome']} HP: {defensor['hp']}.")

            if defensor["hp"] <= 0:
                existe_vencedor = True
                vencedor = atacante
                break

    print("###")

    # Podemos atualizar dicionários utilizando os métodos update ou setdefault
    vencedor.update({"origem": "Terra média"})
    vencedor.setdefault("nome", "Teste")

    for chave, valor in vencedor.items():
        print(f"{chave.capitalize()}: {valor}")

    # Podemos remover um par chave-valor de um dicionário utilizando os métodos pop() ou popitem()
    # pop remove o par chave-valor indicado pelo nome da chave passada como parâmetro
    vencedor.pop("origem")

    # popitem remove o último par chave-valor que foi criado
    vencedor.popitem()

    # Caso queiramos excluir todos os pares chave-valor do dicionário, utilizamos o método clear()
    monstro.clear()

    print(vencedor)
    print(monstro)
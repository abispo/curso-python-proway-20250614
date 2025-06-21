"""
Estruturas de repetição no Python

laço for

Utilizamos o laço for quando queremos iterar sobre um objeto, ou seja, acessar de maneira sequencial os itens desse objeto. Geralmente utilizamos o laço for com listas e tuplas, sendo a condição de interrupção desse laço o fim dos itens a serem lidos.
"""

from random import randint

if __name__ == "__main__":

    """
    Abaixo estamos criando uma lista. Listas são estruturas de dados que armazenam outros tipos de dados, inclusive outras listas. Listas são indexáveis, ordenadas, iteráveis e mutáveis.

    Podemos utilizar 2 formas de criar listas:
    utilizando colchetes ["item1", "item2", "etc"]
    utilizando a função built-in list: list("item1", "item2", "etc")
    """
    lista_compras = ["Banana", "Carne de Frango", "Ovos", "Rollmops", "Manteiga"]

    for item in lista_compras:
        print(item)

    # Dentro do laço for, podemos utilizar alguns comandos especiais, como break e continue

    # O comando break interrompe imediatamente a execução do loop, independentemente de quantos itens faltam para serem lidos
    for item in lista_compras:
        if item == "Rollmops":
            print("Credo! Joga fora.")
            break
        print(item)

    else:
        print("Finalizado")

    # o comando loop interrompe a iteração atual, independentemente de existirem mais intruções a serem executadas no bloco. Ou seja, ele volta para o início do loop para ler o próximo item.
    for coisa in lista_compras:
        if coisa == "Rollmops":
            print("Nem todo mundo gosta de Rollmops. Indo ao próximo item")
            continue
        print(coisa)

    # Em um laço for, podemos utilizar um bloco else. Esse bloco sempre será executado quando o laço for terminar. Caso o loop seja interrompido por uma instrução break, o bloco else não será executado.
    else:
        print("Finalizado")

    # Junto com o laço for, podemos utilizar algumas funções específicas, como a função range() e enumerate()

    print("########## Função range() ##########")

    # A função range() gera números de acordo com os parâmetros informados
    for item in range(10, randint(50, 500), 2):
        print(item, end= ' ')

    print("########## Função enumerate() ##########")
    
    # A função enumerate retorna um par de valores, sendo o primeiro o índice e o segundo o item do objeto sendo iterado.
    for index, item in enumerate(lista_compras, start=1):
        print(f"{index}) {item}")
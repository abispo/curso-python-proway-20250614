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

    """
    Quando dizemos que listas são indexáveis, significa que podemos acessar os valores dessa lista informando uma posição, que chamamos de índice. Por exemplo

    lista = ["Python", "Java", "PHP", "SQL", "Javascript"]
                 0        1      2      3          4
                 -5       -4     -3     -2         -1

    O índice das listas sempre irá começar da posição zero. Ou seja, se quisermos acessar diretamente o terceiro da lista, temos que informar a posição menos 1 (3-1), que será igual ao índice 2.

    Além disso, podemos utilizar índices negativos, com o último item da lista sempre começando com -1
    """

    # Acessando o 4º item da lista
    print(lista_compras[4-1])       # posição na lista menos 1

    # Acessando o último item da lista
    print(lista_compras[-1])

    # Quando utilizamos os índices, temos que nos atentar para a quantidade de itens nessa lista. Caso informemos um índice que não exista na lista, é gerada a exceção IndexError. Por exemplo, a linha abaixo irá gerar essa exceção
    # print(lista_compras[6])

    # Assim como outros tipos de dados, listas também são objetos, e assim como os objetos, podemos utilizar métodos para serem utilizados nessa lista

    # O método append insere um item no final da lista
    lista_compras.append("Cebola")
    lista_compras.append("Tomate")

    # O método insert insere um item na lista na posição informada. No caso abaixo, vai inserir o valor "Queijo" no índice 3 da lista
    lista_compras.insert(3, "Queijo")

    # O método extend insere os itens de um iterável (listas, tuplas, etc) no final da lista atual.
    lista_compras.extend(("Iogurte", "Leite",))

    # Como listas são mutáveis, podemos alterar um valor indicando a posição. Por exemplo, vamos substituir o valor "Rollmops" por "Pimenta"
    lista_compras[4] = "Pimenta"

    # Também podemos utilizar um recurso bem interessante em listas (que também funciona com strings e tuplas), que é o chamado slicing (fatiamento). Podemos extrair uma parte da lista, utilizando para isso os índices
    # Por exemplo, se quisermos pegar os itens da 4ª até a 7ª posição
    print(lista_compras[3:7])

    # Acima estamos pegando os itens "Queijo", "Pimenta", "Manteiga" e "Cebola". Apesar de termos indicado o índice final como 7, quando utilizamos o fatiamento o valor do índice final não será retornado, e sim o valor do índice anterior
    print(lista_compras[:7])
    print(lista_compras[5:])
    print(lista_compras[1:7:3])
    print(lista_compras[::-1])
    print(lista_compras)

    print("############## CÓPIA DE LISTAS ##############")
    # A maneira como estamos fazendo a cópia das listas, irá fazer com que qualquer alteração feita em uma lista seja refletida na outra, pois as 2 variáveis estarão apontando para a mesma posição de memória. Para fazer a cópia correta, podemos utilizar o método copy() ou então o fatiamento de listas
    # lista_laticinios = lista_compras              # Maneira errada
    # lista_laticinios = lista_compras.copy()       # Maneira correta utilizando método
    lista_laticinios = lista_compras[::]            # Maneira correta utilizando fatiamento
    
    # O método pop recebe o índice do item que será removido da lista, e retorna o valor removido. Caso o índice não seja informado, sempre removerá o último item
    lista_laticinios.pop(0)
    lista_laticinios.pop(0)
    lista_laticinios.pop(0)

    # O método remove procura pelo valor informado como parâmetro e o remove da lista
    lista_laticinios.remove("Pimenta")
    lista_laticinios.remove("Cebola")
    lista_laticinios.remove("Tomate")

    print(lista_laticinios)
"""
Operadores em Python

Operadores de atribuição.

Utilizamos operadores de atribuição para atribuir valores que estão à direita em variáveis que estão à esquerda. 
"""

if __name__ == "__main__":

    # Aqui atribuímos o valor que está à direita a variável está à esquerda
    valor = 100

    # Caso queiramos incrementar ou decrementar esse valor, podemos fazer o seguinte:
    valor = valor + 5

    # Porém, podemos utilizar formas curtas de atribuição, por exemplo:
    valor += 15
    valor -= 50
    valor *= 1.5

    print(valor)
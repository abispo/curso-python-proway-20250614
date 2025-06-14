"""
Operadores em Python

Operadores lógicos.

Operadores lógicos são utilizados em conjunto com operadores de comparação em expressões. Podemos combinar várias comparações em um único valor final. Como os operadores de comparação, sempre vai retornar um valor booleano (True ou False). Temos 3 operadores lógicos no Python:

and     -> E
or      -> OU
not     -> NÃO (NEGAÇÃO)
"""

if __name__ == "__main__":

    # Operador and
    # Ele retornará True caso os dois lados da expressão retornem True, se não, retorna False
    print(5 > 4 and 3 > 1)
    print(5 > 4 and 3 < 1)
    print(5 < 4 and 3 > 1)
    print(5 < 4 and 3 < 1)

    print("--------------------")

    # Operador or
    # Ele retornará True caso quaisquer um dos lados da expressão retornem True, se não, retorna False
    print(5 > 4 or 3 > 1)
    print(5 > 4 or 3 < 1)
    print(5 < 4 or 3 > 1)
    print(5 < 4 or 3 < 1)

    print("--------------------")

    # Operador not
    # Esse operador simplesmente nega o valor comparado. Ou seja, se for True ele retorna False, e se for False ele retorna True

    print(not 5 > 4)
    print(not 3 < 1)
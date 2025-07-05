"""
4. Escreva um programa que converta uma lista de inteiros em apenas 1 inteiro. Exemplo:
```
lista = [4, 7, 10, 24]
Saída: 471024
```
"""

from random import randint

if __name__ == "__main__":

    lista_numeros = [randint(1, 20) for _ in range(5)]
    numero_final = ""

    # Transformando a lista de inteiros em um inteiro da maneira "tradicional"

    for numero in lista_numeros:
        numero_final = numero_final + str(numero)

    print(f"Lista inicial: {lista_numeros}")
    print('-'*30)
    print(f"Número final (método tradicional): {numero_final}")

    # Transformando a lista de inteiros em um inteiro utilizando o método join
    print(f"Número final (método join): {''.join([str(numero) for numero in lista_numeros])}")

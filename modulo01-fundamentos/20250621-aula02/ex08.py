"""
8. Escreva um programa em Python que inverta uma lista de números. Exemplo:
```
lista = [4, 7, 8, 1, 9]
lista_invertida = [9, 1, 8, 7, 4]
```
"""

from random import randint

if __name__ == "__main__":
    lista_numeros = [randint(1, 20) for _ in range(10)]

    print(f"Lista original: {lista_numeros}.")

    # Invertendo a lista no método "universal"
    lista_invertida = []

    for numero in lista_numeros:
        lista_invertida.insert(0, numero)

    print(f"Lista invertida método universal: {lista_invertida}")
    print(f"Lista invertida método de fatiamento: {lista_numeros[::-1]}")

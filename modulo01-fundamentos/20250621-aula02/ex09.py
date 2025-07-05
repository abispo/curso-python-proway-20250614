"""
9. Escreva um programa em Python que gere uma lista randômica de 50 números de 1 até 50. Em seguida, retire os valores repetidos dessa lista (utilize a função `randint()` do pacote `random`). Dica: Pesquise sobre o tipo set
"""

from random import randint

if __name__ == "__main__":
    
    lista_numeros = [randint(1, 50) for _ in range(50)]
    lista_sem_repetidos = []

    lista_numeros.sort()
    print(f"Lista original: {lista_numeros}.")

    for numero in lista_numeros:
        if lista_sem_repetidos.count(numero) == 0:
            lista_sem_repetidos.append(numero)

    print(f"Lista sem repetidos método universal: {lista_sem_repetidos}.")
    print(f"Lista sem repetidos utilizando o tipo set: {list(set(lista_numeros))}")

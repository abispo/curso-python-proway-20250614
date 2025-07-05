"""
5. Escreva um programa que gere números randômicos de 0 até 50. Salve esse números em uma lista. Em seguida, informe quais são o maior e o menor número dessa lista. Dica: Utilize as funções built-in `max()` e `min()`
"""

from random import randint

if __name__ == "__main__":

    lista_numeros = [randint(0, 50) for _ in range(10)]

    print(f"Lista gerada: {lista_numeros}")

    # Mostrando o maior e o menor números da lista utilizando max e min
    print("Maior e menor números utilizando max e min:")
    print(f"Maior: {max(lista_numeros)}")
    print(f"Menor: {min(lista_numeros)}")

    # Mostrando o maior e o menor números da lista pela posição
    # Primeiro ordenamos a lista com o método sort
    lista_numeros.sort()
    print("Maior e menor números utilizando a lista ordenada:")
    print(f"Maior: {lista_numeros[-1]}")
    print(f"Menor: {lista_numeros[0]}")

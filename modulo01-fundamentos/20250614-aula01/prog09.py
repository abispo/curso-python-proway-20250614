"""
Laços de condição em Python

if-elif-else

Em Python, o laço de condição mais fundamental, como em outras linguagens, é o laço if-elif-else. Passamos uma expressão para esse laço, e o bloco somente será executado se essa expressão retornar um valor True
"""

# A linha abaixo importa a função randint do módulo random, que faz parte da biblioteca padrão do Python. Diferentemente das funções built-in, que são carregadas e ficam disponíveis imediatamente quando o interpretador é executado, os recursos da biblioteca padrão devem ser importados com a palavra reservada import.
# No caso abaixo, não estamos importando a biblioteca inteira, apenas a função randint, que gerará um número randômico dentro de um intervalo
from random import randint

if __name__ == "__main__":

    numero_sorteado = randint(1, 100)
    numero = int(input("Informe o número que acha que é o sorteado: "))

    print(f"Número sorteado: {numero_sorteado}")

    if numero == numero_sorteado:
        print("Acertou na mosca! Você ganhou 10 pontos!")

    elif numero >= numero_sorteado - 10 and numero <= numero_sorteado + 10:
        print("Bateu na trave! Você ganhou 7 pontos!")

    elif numero >= numero_sorteado - 30 and numero <= numero_sorteado + 30:
        print("Um pouco longe. Você ganhou 3 pontos.")

    else:
        print("Passou longe. Você ganhou 1 ponto.")
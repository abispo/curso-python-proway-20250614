"""
4. Crie um programa que peça ao usuário para digitar dois números inteiros e exiba a soma, subtração, multiplicação e divisão dos números.
"""

if __name__ == "__main__":

    numero1 = int(input("Informe o primeiro número: "))
    numero2 = int(input("Informe o segundo número: "))

    print(f"{numero1} + {numero2} = {numero1 + numero2}")
    print(f"{numero1} - {numero2} = {numero1 - numero2}")
    print(f"{numero1} * {numero2} = {numero1 * numero2}")
    print(f"{numero1} / {numero2} = {numero1 / numero2}")
"""
8. Crie um programa que receba um número inteiro e exiba se ele é par ou ímpar.
"""

if __name__ == "__main__":

    numero = float(input("Informe um número: "))

    print(f"O número {numero} é {'par' if numero % 2 == 0 else 'ímpar'}")
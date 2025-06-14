"""
Tipos de dados em Python

Tipos numéricos.

Em Python, temos 3 tipos numéricos:
* int       -> Para números inteiros
* float     -> Para números com casas decimais
* complex   -> Para números complexos (imaginários)

"""

if __name__ == "__main__":

    base = 10

    numero = int(input("Informe um número: "))
    resultado = numero * base
    print(f"Número vezes a base: {resultado}.")

    # No caso abaixo, mesmo se o resultado da divisão for um número inteiro, será gerado um número com casa decimal (float)
    novo_numero = resultado / 3

    # As vezes, o resultado retornado possui muitas casas decimais, porém podemos arredondar esse valor. Abaixo, estamos limitando a quantidade de casas decimais a apenas uma
    print(f"{novo_numero:.1f}")

    # Números complexos são números que possuem uma parte real e a outra imaginária
    numero_complexo = 45j

    print(numero_complexo)
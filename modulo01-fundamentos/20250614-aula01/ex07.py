"""
7. Faça um programa que receba uma temperatura em graus Celsius e exiba a temperatura equivalente em graus Fahrenheit. A fórmula de conversão é: Fahrenheit = (Celsius * 9/5) + 32.
"""

if __name__ == "__main__":

    celsius = float(input("Informe a temperatura em graus Celsius: "))
    fahrenheit = (celsius * (9/5)) + 32

    print(f"{celsius}ºC equivalem a {fahrenheit:.1f}ºF.")
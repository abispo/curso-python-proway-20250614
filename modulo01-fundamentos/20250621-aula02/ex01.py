"""
1. Escreva um programa que receba um número maior do que 1 pelo terminal. Em seguida, o programa retorna a soma de 1 até esse número. Ex:

```
Informe o número: 5
A soma de 1 até 5 é 15
```
"""

if __name__ == "__main__":

    numero = int(input("Informe um número: "))

    soma = 0

    for seq in range(1, numero+1):
        soma = soma + seq

    print(f"A soma de 1 até {numero} é igual a {soma}.")
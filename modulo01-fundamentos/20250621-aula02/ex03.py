"""
3. Escreva um programa que gere 100 números randômicos de 1 a 100. Em seguida, crie 2 listas: Uma que irá salvar apenas os números pares, e outra que irá salvar apenas os números ímpares. Em seguida, mostre na tela a quantidade de itens de cada lista e quais são os seus valores. Exemplo:
```
Itens na lista de pares: 5
Valores: [2, 8, 20, 50, 4]

Itens na lista de ímpares: 4
lista_impares = [45, 79, 3]
```
"""

from random import randint

if __name__ == "__main__":

    lista_pares = []
    lista_impares = []

    for _ in range(100):
        
        numero = randint(1, 100)

        if numero % 2 == 0:
            lista_pares.append(numero)
        else:
            lista_impares.append(numero)

    print(f"Quantidade de itens na lista de pares: {len(lista_pares)}")
    print(f"Valores: {lista_pares}")
    print('-'*50)
    print(f"Quantidade de itens da lista de ímpares: {len(lista_impares)}")
    print(f"Valores: {lista_impares}")
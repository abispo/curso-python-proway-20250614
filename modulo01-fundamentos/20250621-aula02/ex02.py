"""
2. Escreva um programa que receba números pelo terminal. Se o usuário digitar o número 0, o programa para de receber números pelo terminal e retorna uma lista dos quadrados desses números. Exemplo:
```
Digite um número: 4
Digite um número: 2
Digite um número: 6
Digite um número: 0

Lista dos quadrados: [16, 4, 36]
```
"""

if __name__ == "__main__":

    lista_numeros = []

    while True:
        numero = int(input("Informe um número (0 para sair): "))

        if numero == 0:
            break

        lista_numeros.append(numero)

    print(f"Lista original: {lista_numeros}")

    # Criando a lista de quadrados utilizando o método "tradicional"
    lista_quadrados = []
    for item in lista_numeros:
        lista_quadrados.append(item * item)
    print(f"Lista de quadrados (método tradicional): {lista_quadrados}")

    # Criando a lista de quadrados utilizando list-comprehension
    lista_quadrados2 = [item*item for item in lista_numeros]
    print(f"Lista de quadrados (list-comprehension): {lista_quadrados2}")
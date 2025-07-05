"""
7. Escreva um programa que receba nome, idade e gênero de 5 usuários. Em seguida, mostre quantos usuários são do gênero masculino, quantos são do gênero feminino e qual é a média de idade. Exemplo:
```
Nome: João
Idade: 32
gênero: M

Nome: Maria
Idade: 17
gênero: F

Nome: Vanessa
Idade: 28
gênero: F

Quantidade de usuários do gênero masculino: 1
Quantidade de usuários do gênero feminino: 2
Média de idade: 25.67
```
"""

if __name__ == "__main__":

    lista_usuarios = []
    for _ in range(5):
        
        nome = input("Informe o nome do usuário: ")
        idade = int(input("Informe a idade do usuário: "))
        genero = input("Informe o gênero do usuário (M/F): ")

        lista_usuarios.append({
            "nome": nome,
            "idade": idade,
            "genero": genero
        })

    # qtd_masculino = len([item for item in lista_usuarios if item.get("genero") == "M"])
    qtd_masculino = 0
    qtd_feminino = 0
    soma_idade = 0

    for usuario in lista_usuarios:
        if usuario.get("genero") == 'M':
            qtd_masculino += 1          # qtd_masculino = qtd_masculino + 1
        else:
            qtd_feminino += 1           # qtd_feminino = qtd_feminino + 1

        soma_idade = soma_idade + usuario.get("idade")

    print(f"Quantidade de usuários do gênero masculino: {qtd_masculino}.")
    print(f"Quantidade de usuários do gênero feminino: {qtd_feminino}.")
    print(f"Média de idade: {soma_idade / len(lista_usuarios):.1f}.")
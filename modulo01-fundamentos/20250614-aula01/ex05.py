"""
5. Escreva um programa que solicite o nome, a idade e o gênero do usuário. Em seguida, exiba uma mensagem personalizada informando se o usuário é do gênero masculino ou feminino e se é maior ou menor de idade.
"""

if __name__ == "__main__":

    nome = input("Informe o seu nome: ")
    idade = int(input("Informe a sua idade: "))
    i_genero = input("Informe o seu gênero (M ou F): ")

    genero = "Masculino" if i_genero.upper() == 'M' else "Feminino"
    texto_idade = "maior de idade" if idade >= 18 else "menor de idade"

    print(f"Olá {nome}. Você é {texto_idade} e do gênero {genero}.")

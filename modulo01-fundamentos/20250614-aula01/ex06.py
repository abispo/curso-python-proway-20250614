"""
6. Crie um programa que leia três notas (nota1, nota2 e nota3) de um aluno e calcule a média. Se a média for menor do que 5, imprima a mensagem "Reprovado". Se a média for maior ou igual a 5 e menor do que 7, imprima "em recuperação". Se a média for maior ou igual a 7, imprima "Aprovado".
"""

if __name__ == "__main__":

    nota1 = float(input("Informe a primeira nota: "))
    nota2 = float(input("Informe a segunda nota: "))
    nota3 = float(input("Informe a terceira nota: "))

    media = (nota1 + nota2 + nota3) / 3

    if media < 5:
        # O parâmetro end substitui a quebra de linha por outro caractere. Nesse caso, por um espaço em branco.
        print("O aluno foi reprovado", end=' ')

    elif media >= 5 and media < 7:
        print("O aluno está de recuperação", end=' ')

    else:
        print("O aluno foi aprovado", end=' ')

    # Abaixo estamos formatando a saída do número, limitando a apenas 1 dígito após o ponto
    print(f"com a média {media:.1f}")
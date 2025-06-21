"""
10. Escreva um programa que leia o salário de um funcionário e exiba o valor do salário líquido, descontando o INSS. As faixas de desconto são as seguintes:
* Até R$ 1.320,00                   7,5%
* De R$ 1.320,01 a R$ 2.571,29 	    9%
* De R$ 2.571,30 até R$ 3.856,94 	12%
* Acima de R$ 3.856,95              14%
"""

if __name__ == "__main__":

    PRIMEIRA_FAIXA = 0.075
    SEGUNDA_FAIXA = 0.09
    TERCEIRA_FAIXA = 0.12
    QUARTA_FAIXA = 0.14

    salario_bruto = float(input("Informe o seu salário bruto: "))
    salario_liquido = 0
    desconto = 0

    if salario_bruto < 1320:
        desconto = salario_bruto * PRIMEIRA_FAIXA
        salario_liquido = salario_bruto - desconto
        faixa_de_desconto = "7.5%"

    elif salario_bruto >= 1320.01 and salario_bruto < 2571.29:
        desconto = salario_bruto * SEGUNDA_FAIXA
        salario_liquido = salario_bruto - desconto
        faixa_de_desconto = "9.0%"

    elif (salario_bruto >= 2571.30 and salario_bruto < 3856.94):
        desconto = salario_bruto * TERCEIRA_FAIXA
        salario_liquido = salario_bruto - desconto
        faixa_de_desconto = "12.0%"

    else:
        desconto = salario_bruto * QUARTA_FAIXA
        salario_liquido = salario_bruto - desconto
        faixa_de_desconto = "14.0%"

    print(f"Seu salário bruto é de R${salario_bruto:.2f}.")
    print(f"Foram descontados R${desconto:.2f} do seu salário, sendo a faixa de desconto de {faixa_de_desconto}.")
    print(f"Seu salário líquido é de R${salario_liquido:.2f}.")
"""
9. Crie um programa que receba o nome, o peso e a altura de uma pessoa. Em seguida, calcule o seu IMC. A altura deve ser informada no formato `metros.centimetros` (exemplo 1.79). A fórmula do IMC é a seguinte: peso / (altura * altura).
"""

if __name__ == "__main__":

    nome = input("Informe o seu nome: ")
    peso = float(input("Informe o seu peso em KG: "))
    altura = float(input("Informe sua altura em metros: "))

    imc = peso / (altura * altura)

    print(f"{nome}, você mede {altura}m e tem {peso}kg, o que resulta em um IMC de {imc:.1f}.")
"""
Funções (Procedures)

Também podemos passar valores para a função utilizando os parâmetros (ou argumentos). Esses valores serão acessíveis dentro da função.
"""

# Apesar de não ser obrigatório, podemos indicar os tipos dos parâmetros e de retorno da função. Como Python é uma linguagem dinamicamente tipada, mesmo informando os tipos, isso não significa que eles serão checados em tempo de execução.
def calculo_imc(altura: float, peso: float) -> float:
    return peso / (altura * altura)

if __name__ == "__main__":

    # Estamos passando os valores para a função de maneira posicional, ou seja, a ordem dos valores deve refletir os valores esperados pelos parâmetros
    print(f"{calculo_imc(1.88, 92.3):.1f}")

    # Porém podemos passar os valores indicando quais parâmetros que irão recebê-los. Dessa maneira, não precisamos seguir a ordem dos parâmetros
    print(f"{calculo_imc(peso=87.5, altura=1.79):.1f}")

    # Também podemos utilizar as 2 maneiras em conjuntos, porém sempre devemos passar os valores dos parâmetros opcionais primeiro e pelo nome dos parâmetros depois, nunca o nome antes da posição
    # func(param1=10, 13, "Ok") # Errado
    # func(13, "Ok", param1=10) # Certo

    # Existe um recurso bastante útil no Python, que é o chamado desempacotamento de valores. Basicamente utilizamos uma sintaxe especial para passar valores de uma sequência diretamente nos parâmetros de uma função.

    altura_peso_alberto = (1.81, 101.2,)

    # Normalmente, passaríamos os valores para a função dessa maneira:
    print("{:.1f}".format(
        calculo_imc(altura_peso_alberto[0], altura_peso_alberto[1]))
    )

    # Ao invés de utilizar a linha acima, vamos desempacotar os valores nos parâmetros. É importante mencionar que a quantidade de valores da sequência deve ser exatamente igual a quantidade de parâmetros obrigatórios da função
    print("{:.1f}".format(
        calculo_imc(*altura_peso_alberto))
    )

    print('-'*50)

    # Cenário onde temos uma lista de valores
    lista_alturas_pesos = [
        (1.65, 53.3,),
        (1.77, 68.9,),
        (1.78, 80.1,),
        (1.99, 91.9,),
        (1.74, 83.6,)
    ]
    for item in lista_alturas_pesos:
        print("{:.1f}".format(
        calculo_imc(*item))
    )
        
    print('-'*50)
        
    # Também podemos desempacotar os valores de um dicionário. Dessa maneira, estamos passando os valores para a função utilizando os nomes dos parâmetros
    altura_peso_roberto = {"altura": 1.74, "peso": 107.3}
    print("{:.1f}".format(
        calculo_imc(**altura_peso_roberto)
    ))

    print('-'*30)

    lista_alturas_pesos = [
        {"altura": 1.88, "peso": 98.6},
        {"peso": 101.5, "altura": 2.03},
        {"peso": 99.4, "altura": 1.93},
        {"peso": 62.5, "altura": 1.64},
        {"altura": 1.77, "peso": 80.1}
    ]

    for item in lista_alturas_pesos:
        print("{:.1f}".format(
        calculo_imc(**item))
    )
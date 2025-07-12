"""
Funções (procedures)

No Python, é possível criarmos funções que recebem uma quantidade arbitrária de funções ou parâmetros. Ou seja, podemos chamar uma função passando quantos valores quisermos para ela. Podemos chamar também de empacotamento de valores.
"""

# Utilizamos o padrão *args para indicar que uma função pode receber uma quantidade indeterminada de valores de maneira posicional
def calculo_media_leitura(*args) -> float:
    return sum(args) / len(args)


def mostra_info(**kwargs):
    for chave, valor in kwargs:
        print(f"{chave}: {valor}")

    print('*'*30)


if __name__ == "__main__":
    # Passamos os valores para a função de maneira posicional.
    print(calculo_media_leitura(0.6, 0.7, 0.5, 0.9))
    print(calculo_media_leitura(0.6, 0.7))
    print(calculo_media_leitura(0.6, 0.7, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 1))

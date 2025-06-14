# Tipos de dados em Python

# strings
# Strings basicamente são textos, ou cadeias de caracteres que podem possuir qualquer caractere.

if __name__ == "__main__":
    
    print("Strings podem ser definidas utilizando aspas duplas ou simples.")
    print('Também podemos utilizar aspas dentro de aspas, "dessa maneira".')
    print("Ou então utilizando \"marcaco\tes esp\neciais\".")

    print("""
Também podemos utilizar strings multi-linha.
          
          Toda a formatação que for definida nessa string, será mantida caso ela seja impressa no

  terminal
""")

    # Pra concatenas strings em Python, podemos utilizar algumas abordagens

    # 1. Utilização do sinal +
    print("Olá! o curso é sobre " + "Python" + " e começa no " + "sábado.")

    # 2. Utilizando o estilo antigo do Python 2
    print("Olá %s. Sua nota final foi de %f" % ("Barbara", 8.5,))

    # 3. Utilizando o método format
    print("A prova final do curso {} será em {}".format("Java Web", "14/07/2025"))
    # Também podemos passar os nomes dos parâmetros que substituirão os valores
    print("No dia {dia_inicial} foram processados {qtd_arquivos} arquivos.".format(
        dia_inicial="04/08/2025", qtd_arquivos=7490
    ))

    # Utilizando f-strings
    # Qualquer expressão válida em Python pode ser colocada dentro das chaves. Uma expressão é um comando ou conjunto de comandos que irão retornar um valor. No caso abaixo, utilizamos a estrutura if else junto com operadores lógicos e aritméticos para retornar um valor que será concatenado no restante da string.
    print(f"O resultado do cálculo é {'Positivo' if (5 + 10 * (15 / 3)) >= (14 + 3 / (5 ** 5)) else 'Negativo'}")

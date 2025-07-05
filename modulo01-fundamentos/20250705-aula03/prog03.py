"""
Funções (Procedures)

Também é possível criar funções que possuem parâmetros opcionais, ou seja, parâmetros que não precisam receber um valor. Para isso, devemos definir um valor padrão para esses parâmetros
"""

def calculo_hora_extra(valor_hora: float, qtd_horas_extras: int = 0) -> float:
    return valor_hora * qtd_horas_extras

if __name__ == "__main__":
    print("{:.2f}".format(calculo_hora_extra(56, 3)))
    print("{:.2f}".format(calculo_hora_extra(qtd_horas_extras=1, valor_hora=60)))

    # Como não passamos nenhum valor para o parâmetro qtd_horas_extras, será considerado o valor padrão de 0
    print("{:.2f}".format(calculo_hora_extra(20)))
    print("{:.2f}".format(calculo_hora_extra(valor_hora=40)))
"""
Funções (Procedures)

Funções são blocos de código que executam uma determinada tarefa. Devido a sua natureza, funções são definidas 1 vez e utilizadas em diversas partes do código. Além disso, funções podem receber valores através de parâmetros e também podem retornar valores resultantes das tarefas realizadas. A utilização de funções facilita o reuso de código.

Em python, utilizamos a palavra reservada 'def' para criar funções.
"""

# Utilizamos o módulo datetime quando queremos trabalhar com data/hora no Python.
from datetime import datetime

def detalhe_data_hora_agora():
    print(datetime.now().strftime(
        "%H:%M %d/%m/%Y"                    # https://strftime.org/
    ))

if __name__ == "__main__":
    detalhe_data_hora_agora()

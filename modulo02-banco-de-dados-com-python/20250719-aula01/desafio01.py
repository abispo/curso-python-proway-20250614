"""
Os arquivos estão em https://github.com/abispo/shared-files/tree/main/modulo02. Utilize a biblioteca requests para baixá-los.

Ler o arquivo cursos.csv e salvar os dados na tabela tb_cursos. Essa tabela deve ter a seguinte estrutura.

id              INT         PRIMARY KEY AUTOINCREMENT
curso           VARCHAR     NOT NULL
carga_horaria   INT         NOT NULL
preco           FLOAT       NOT NULL
Após os dados terem sido salvos, vamos criar uma nova tabela chamada tb_estatisticas_cursos, que terá as seguintes colunas:

qtd_cursos                  INT
curso_maior_carga_horaria:  VARCHAR
curso_com_maior_valor:      VARCHAR

Após salvar, mostrar esses dados na tela. Exemplo:

Quantidade de cursos: 10
Curso com a maior carga horária: Web Development com Django (50 horas)
Curso com o maior valor: Machine Learning Fundamentals (R$ 1200.00)
"""
import csv
import os

from dotenv import load_dotenv

import pymysql
import requests

load_dotenv()

if __name__ == "__main__":

    url = "https://raw.githubusercontent.com/abispo/shared-files/refs/heads/main/modulo02/cursos.csv"

    response = requests.get(url)
    content = response.text

    # r -> somente leitura
    # w -> somente escrita com truncate (apaga o conteúdo do arquivo e sobrescreve)
    # a -> somente escrita a partir do final do arquivo (mantém o conteúdo)
    with open(os.path.join(os.getcwd(), "cursos.csv"), 'w', encoding='utf-8') as _file:
        _file.write(content)

    connection = pymysql.connect(
        user=os.getenv("DATABASE_USER"),
        password=os.getenv("DATABASE_PASSWORD"),
        host=os.getenv("DATABASE_HOST"),
        port=int(os.getenv("DATABASE_PORT")),
        database=os.getenv("DATABASE_NAME")
    )
    cursor = connection.cursor()

    command = """
        CREATE TABLE IF NOT EXISTS tb_cursos(
            id INT PRIMARY KEY AUTO_INCREMENT,
            curso VARCHAR(100) NOT NULL,
            carga_horaria INT NOT NULL,
            preco FLOAT NOT NULL
        );"""
    
    cursor.execute(command)
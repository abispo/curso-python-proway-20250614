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

    command = """
        CREATE TABLE IF NOT EXISTS tb_estatisticas_cursos(
            id INT PRIMARY KEY AUTO_INCREMENT,
            qtd_cursos INT NOT NULL,
            curso_maior_carga_horaria VARCHAR(100) NOT NULL,
            curso_com_maior_valor VARCHAR(100) NOT NULL
        );"""
    cursor.execute(command)

    cursor.execute("DELETE FROM tb_estatisticas_cursos")
    cursor.execute("DELETE FROM tb_cursos")
    connection.commit()

    # A linha abaixo considera que o arquivo cursos.csv está na mesma pasta que o script
    with open("cursos.csv", "r", encoding="utf-8") as _file:

        csv_file = csv.DictReader(_file, delimiter=';')

        for line in csv_file:
            command = """
                INSERT INTO tb_cursos(curso, carga_horaria, preco) VALUES(
                    '{}', {}, {}
                )""".format(
                    line.get("curso"),
                    int(line.get("carga_horaria")),
                    float(line.get("preco"))
                )
            cursor.execute(command)
        connection.commit()

    # Agora iremos salvar os dados estatísticos. Podemos utilizar tanto SQL quanto Python para gerar essas informações. Vamos passar pelos 2 métodos

    # Método 1: Utilizando SQL

    # Quantidade de cursos
    cursor.execute(
        "SELECT COUNT(id) FROM tb_cursos"
    )
    qtd_cursos = cursor.fetchone()[0]

    # Curso com a maior carga horária
    cursor.execute(
        "SELECT * FROM tb_cursos ORDER BY carga_horaria DESC"
    )
    curso_maior_carga_horaria = cursor.fetchone()

    # Curso com o maior valor
    cursor.execute(
        "SELECT * FROM tb_cursos ORDER BY preco DESC;"
    )
    curso_com_maior_valor = cursor.fetchone()

    command = """
        INSERT INTO tb_estatisticas_cursos(
            qtd_cursos, curso_maior_carga_horaria, curso_com_maior_valor
        ) VALUES ({}, '{}', '{}');""".format(
            qtd_cursos,
            f"{curso_maior_carga_horaria[1]} ({curso_maior_carga_horaria[2]} horas)",
            f"{curso_com_maior_valor[1]} (R$ {curso_com_maior_valor[3]})"
        )
    cursor.execute(command)
    connection.commit()

    # Método 2: Utilizando Python
    cursor.execute("SELECT * FROM tb_cursos")
    results = cursor.fetchall()

    cursor.close()
    connection.close()

    # Quantidade de cursos
    qtd_cursos2 = len(results)
    print(qtd_cursos2)

    # Curso com a maior carga horário
    curso_maior_carga_horaria = sorted(
        results, key=lambda item: item[2], reverse=True
    )[0]

    curso_maior_valor2 = sorted(
        results, key=lambda item: item[3], reverse=True
    )[0]

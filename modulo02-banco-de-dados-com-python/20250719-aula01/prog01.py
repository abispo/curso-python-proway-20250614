"""
Python com banco de dados

Assim como em outras linguagens, podemos utilizar o Python para acesso a vários tipos de bancos de dados. Isso é feito utilizando uma biblioteca de acesso, que também podemos chamar de conector. Através dessa biblioteca é que definimos e enviamos os comandos SQL que serão executados no banco de dados.

Por padrão, o Python já tem com uma biblioteca que permite trabalhar com o banco de dados SQLite.
"""

import os
import sqlite3

if __name__ == "__main__":
    
    """
    Geralmente, quando queremos conectar nossa aplicação a um banco de dados, seguimos o seguinte passo-a-passo

    1. Definimos a connection string do banco. Connection string nada mais é do que um texto com as informações necessárias para acessar o banco de dados: usuario, senha, endereço, etc..
    2. Criamos uma conexão com o banco de dados a partir da connection string
    3. A partir da conexão, criamos um cursor. É através do cursor que enviamos os comandos SQL para o banco de dados
    4. Executamos o cursor, e se necessário pegamos o resultado do comando no banco de dados.
    5. Fechamos o cursor e a conexão
    """

    # 1. Definimos a connection string
    connection_string = os.path.join(os.getcwd(), "db.sqlite3")

    # 2. Criamos a conexão com o banco utilizando a connection string
    connection = sqlite3.connect(connection_string)

    # 3. Criação do cursor que será utilizado para executar os comandos SQL
    cursor = connection.cursor()

    # Nesse momento, já podemos utilizar o cursor para executar os comandos.
    # Vamos criar a tabela tb_cursos
    comando = """
        CREATE TABLE IF NOT EXISTS tb_cursos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL
        );
"""

    # 4. Executamos o comando definido anteriormente utilizando o cursor
    response = cursor.execute(comando)

    lista_cursos = [
        {"nome": "Fundamentos Python", "preco": 550},
        {"nome": "Java Avançado", "preco": 1500},
        {"nome": "Microserviços com Go", "preco": 990},
        {"nome": "Introdução ao DevOps", "preco": 600},
        {"nome": "Linux Básico", "preco": 750}
    ]

    for curso in lista_cursos:
        comando = "INSERT INTO tb_cursos(nome, preco) VALUES ('{nome}', {preco})".format(
            **curso
        )

        # Apenas o método execute() não irá salvar os dados na tabela. No caso de comandos DML (Data Manipulation Language) INSERT, DELETE e UPDATE precisamos confirmar a transação para que os dados sejam salvos. Nesse caso, precisamos executar o método commit() da conexão, que irá confirmar essa transação. https://miro.medium.com/v2/resize:fit:600/1*Hzxwsot3CEX5C1Auh4e77g.png
        # cursor.execute(comando)
    
    # Confirmação da transação
    # connection.commit()

    # Agora vamos consultar os dados da tabela. Podemos utilizar 3 métodos para trazer os dados de uma tabela no banco.

    # fetchone(): Retorna apenas 1 registro da tabela. Se a consulta não tiver resultados, retorna None. Caso haja resultados, esse método retorna uma tupla, onde cada item da tupla é o valor da coluna

    command = "SELECT * FROM tb_cursos;"
    cursor.execute(command)

    response = cursor.fetchone()
    print(response)

    # fetchmany(qtd): Retorna a quantidade de registros que é informada como uma lista de tuplas. Se a consulta não trouxer resultados, retorna uma lista vazia
    response = cursor.fetchmany(2)
    print(response)

    # fetchall(): Retorna todos os resultados da consulta. Se a consulta não tiver resultados, retorna uma lista vazia
    response = cursor.fetchall()
    print(response)

    print(cursor.fetchall())

    # 5. Fechamos o cursor e a conexão
    cursor.close()
    connection.close()

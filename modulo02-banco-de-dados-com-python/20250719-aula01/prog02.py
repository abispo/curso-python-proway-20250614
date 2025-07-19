# https://api.coinlore.net/api

import os

import pymysql
import pymysql.cursors
import requests

from dotenv import load_dotenv

# Essa função carrega os pares chave-valor do arquivo .env e os transforma em variáveis de ambiente e seus valores
load_dotenv()

if __name__ == "__main__":

    conexao = pymysql.connect(
        user=os.getenv("DATABASE_USER"),
        password=os.getenv("DATABASE_PASSWORD"),
        host=os.getenv("DATABASE_HOST"),
        port=int(os.getenv("DATABASE_PORT")),
        database=os.getenv("DATABASE_NAME")
    )
import os

import pymysql
import pymysql.cursors
import requests

from dotenv import load_dotenv

# Essa função carrega os pares chave-valor do arquivo .env e os transforma em variáveis de ambiente e seus valores
load_dotenv()

if __name__ == "__main__":

    connection = pymysql.connect(
        user=os.getenv("DATABASE_USER"),
        password=os.getenv("DATABASE_PASSWORD"),
        host=os.getenv("DATABASE_HOST"),
        port=int(os.getenv("DATABASE_PORT")),
        database=os.getenv("DATABASE_NAME")
    )

    cursor = connection.cursor()

    command = """
        CREATE TABLE IF NOT EXISTS tb_criptos(
            id INT PRIMARY KEY AUTO_INCREMENT,
            simbolo VARCHAR(10) NOT NULL,
            nome VARCHAR(20) NOT NULL,
            preco_usd DOUBLE NOT NULL,
            market_cap_usd DOUBLE NOT NULL,
            criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
"""

    cursor.execute(command)

    # URL da API
    url = "https://api.coinlore.net/api"

    cripto_id = input("Informe o código da moeda: ")
    response = requests.get(
        f"{url}/ticker?id={cripto_id}"
    )

    ticker_info = response.json()[0]

    command = """
        INSERT INTO tb_criptos(simbolo, nome, preco_usd, market_cap_usd)
        VALUES
        (%s, %s, %s, %s)"""
    
    cursor.execute(
        command,
        (
            ticker_info.get("symbol"),
            ticker_info.get("name"),
            ticker_info.get("price_usd"),
            ticker_info.get("market_cap_usd"),
        )
    )

    connection.commit()

    print(ticker_info)
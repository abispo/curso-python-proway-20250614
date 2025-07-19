# https://api.coinlore.net/api

import pymysql
import pymysql.cursors
import requests

if __name__ == "__main__":

    conexao = pymysql.connect(
        user="root",
        password="admin",
        host="127.0.0.1",
        port=3306,
        database="criptomoedas"
    )
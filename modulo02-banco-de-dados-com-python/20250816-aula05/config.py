import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, DeclarativeBase

# Carreta as variáveis de ambiente a partir do arquivo .env
load_dotenv()

# Definimos a connection string da aplicação
connection_string = os.getenv("DATABASE_URL")

# Abaixo criamos o objeto de conexão ao banco de dados. O parâmetro echo=True define que o programa vai mostrar na mensagem de debug o comando SQL que será enviado ao banco de dados
connection = create_engine(connection_string, echo=True)

# Abaixo criamos a sessão de acesso ao nosso banco de dados. É a partir da sessão que os comandos serão enviados ao banco de dados
session = scoped_session(sessionmaker(
    bind=connection
))

# Aqui criamos a classe Base que será herdada por todas as nossas models do projeto. O termo Model refere-se a uma classe que está mapeando uma tabela no banco de dados.
class Base(DeclarativeBase):
    pass
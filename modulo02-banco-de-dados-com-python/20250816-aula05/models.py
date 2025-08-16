from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from config import Base

# Aqui criamos a classe que será mapeada para a tabela users no banco de dados. Total model obrigatoriamente deve herdar da classe Base
class User(Base):

    # A propriedade __tablename__ define o nome da tabela no banco de dados
    __tablename__ = "users"

    # Abaixo estamos criando os atributos da classe User, que serão mapeados como as colunas da tabela users. A sintaxe que estamos utilizando é a da versão 2.* do SQLAlchemy. Na versão 1.*, não utilizamos a tipagem com Mapped e ao invés de mapped_column, utilizamos a classe Column.
    # Aqui estamos criando a coluna id, que será do tipo int, chave primária e auto incremento
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    
    # Coluna email, do tipo varchar(100) e que não permite valores nulos
    email: Mapped[str] = mapped_column(String(100), nullable=False)

    password: Mapped[str] = mapped_column(String(100), nullable=False)

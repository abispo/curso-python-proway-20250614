from datetime import date
from typing import List

from sqlalchemy import Integer, String, ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

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

    # Abaixo estamos criando a propriedade profile que será do tipo relationship. Com isso, podemos criar uma relação entre as instâncias User e Profile (desde que exista uma chave estrangeira ligando as tabelas), ou seja, podemos carregar os dados do perfil do usuário fazendo a chamada user.profile. O atributo profile nesse caso sera a instância da classe Profile. Podemos fazer também profile.user, que por sua vez irá carregar os dados de usuário associados ao perfil
    profile: Mapped["Profile"] = relationship(back_populates="user")

    posts: Mapped[List["Post"]] = relationship(back_populates="user")

    def __str__(self):
        return f"<User({self.id}, {self.email})>"
    
    def __repr__(self):
        return f"<User({self.id}, {self.email})>"


class Profile(Base):

    __tablename__ = "profiles"

    # Abaixo estamos criando a coluna id da tabela profiles como chave primária e chave estrangeira da coluna id da tabela users. Utilizamos a classe ForeignKey para criar essa chave estrangeira. E como valor passamos [nome_da_tabela.nome_da_coluna]
    id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    birth_date: Mapped[date] = mapped_column(Date, nullable=True)
    gender: Mapped[str] = mapped_column(String(100), nullable=True)

    user: Mapped["User"] = relationship(back_populates="profile")


class Post(Base):

    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    content: Mapped[str] = mapped_column(String(1000), nullable=False)

    user: Mapped["User"] = relationship(back_populates="posts")
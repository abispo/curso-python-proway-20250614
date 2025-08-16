from sqlalchemy import select

from config import session

from models import User, Profile

menu = """
=== MENU USUÁRIOS ===

Informe a opção desejada:

1. Selecionar Usuários
2. Inserir Usuários
3. Atualizar Usuários
4. Remover Usuários
0. Voltar
"""

def users_management():
    while True:
        print(menu)

        option = int(input("Informe a opção: "))

        match option:
            case 0:
                break

            case 1:
                select_users()

            case 2:
                email = input("Informe o e-mail do usuário: ")
                password = input("Informe a senha do usuário: ")
                name = input("Informe o nome do usuário: ")
                birth_date = input("Informe a data de nascimento do usuário (Formato YYYY-MM-DD): ")
                gender = input("Informe o gênero do usuário: ")

                insert_users(
                    email=email, password=password, name=name, birth_date=birth_date, gender=gender
                )

def select_users():

    # Abaixo estamos utilizando a função select(), que faz parte do SQLALchemy core. Ela será responsável por gerar o comando SELECT FROM no banco de dados
    stmt = select(User)

    # Agora estamos utilizando o método execute do objeto de sessão para executar esse comando no banco de dados. O método scalars() retorna um objeto iterável, ou seja, para ter acesso aos dados, precisamos utilizar o laço for. O método all() retorna uma lista dos objetos User.
    # Geralmente utilizamos o scalars quando queremos retornar apenas algumas colunas e o all quando queremos retornar todo o objeto.
    users = session.execute(stmt).scalars().all()

    if len(users) == 0:
        print("Não existem usuários cadastrados.")
        return

    for user in users:
        print(f"{user.email}")


def insert_users(
        email: str,
        password: str,
        name: str,
        birth_date: str | None = None,
        gender: str | None = None):
    
    user = User(email=email, password=password)
    session.add(user)
    session.commit()
    
    profile = Profile(id=user.id, name=name, birth_date=birth_date, gender=gender)
    session.add(profile)
    session.commit()

    print(f"Usuário '{user.email}' inserido com sucesso!")
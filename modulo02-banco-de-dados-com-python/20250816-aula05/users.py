from sqlalchemy import select

from config import session

from models import User

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

def select_users():

    stmt = select(User)

    users = session.execute(stmt).scalars().all()

    if len(users) == 0:
        print("Não existem usuários cadastrados.")
        return

    for user in users:
        print(f"{user.email}")
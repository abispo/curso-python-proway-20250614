from config import connection
from models import *            # Importa tudo de models

from users import users_management

if __name__ == "__main__":
    Base.metadata.create_all(connection)

    menu = """
=== MENU PRINCIPAL ===

Informe a opção desejada:

1. Gerenciar Usuários
2. Gerenciar Postagens
3. Gerenciar Categorias
4. Gerenciar Comentários
0. Sair
"""

    while True:
        print(menu)
        option = int(input("Informe a opção: "))

        match option:
            case 0:
                print("Saindo...")
                break

            case 1:
                users_management()

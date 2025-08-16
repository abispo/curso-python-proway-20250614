from config import connection
from models import *            # Importa tudo de models

if __name__ == "__main__":
    Base.metadata.create_all(connection)
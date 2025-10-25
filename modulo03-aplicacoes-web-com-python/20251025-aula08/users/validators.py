from datetime import datetime, date
from typing import Union

# O Union indica que a função pode retornar ou um objeto date, ou um valor nulo.
# Também podemos utilizar a sintaxe -> date | None
def parse_date(birth_date: str) -> Union[date, None]:
    try:
        return datetime.strptime(
            birth_date, "%Y-%m-%d"
        ).date()
    except Exception:
        return None

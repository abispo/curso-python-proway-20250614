"""
Funções (Procedures)

Também é possível criar funções que podem chamar a si mesmas. Chamamos essas funções de funções recursivas. Esse tipo de função não é uma exclusividade do Python, podendo ser implementada na maioria das linguagens.

Vamos utilizar como exemplo a função fatorial (n!)
"""

def fatorial_nao_recursivo(numero: int) -> int:
    contador = numero
    total = numero

    while contador > 1:
        total = total * (contador - 1)
        contador = contador - 1

    return total


def fatorial_recursivo(numero: int) -> int:
    if numero == 1:
        return numero
    
    return numero * fatorial_recursivo(numero - 1)

if __name__ == "__main__":

    print(f"Fatorial de 5 (não recursivo): {fatorial_nao_recursivo(5)}")
    print(f"Fatorial de 10 (não recursivo): {fatorial_nao_recursivo(10)}")

    print('*'*30)
    
    print(f"Fatorial de 5 (recursivo): {fatorial_recursivo(5)}")
    print(f"Fatorial de 10 (recursivo): {fatorial_recursivo(10)}")
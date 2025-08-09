"""
Programação Orientada a Objetos

Classes, objetos, atributos e métodos
"""

# Para criar uma classe em Python, utilizamos a palavra reservada class.
# Quando criamos uma classe, estamos criando um novo bloco de código. Ou seja, precisamos respeitar o espaçamento de 4 caracteres.
# De preferência, os nomes das classes devem seguir o padrão PascalCase. Ou seja, o nome começa com letra maiúscula, e se for um nome composto, cada palavra deve também começar com maiúscula.
class Pokemon:

    # O método __init__ é um método especial em Python que serve para inicializar os atributos de uma classe. Nesse método podemos passar os valores que serão passados para os atributos
    # Nos métodos de instância em Python, obrigatoriamente precisamos passar como primeiro atributo dos métodos, o self, que nada mais é que uma referência ao objeto que está sendo instanciado.
    # Além disso, estamos tipando os parâmetros do método, ou seja, defifindo os tipos de valores que devem ser passados.
    def __init__(self, nome: str, tipo: str, saude: int):
        self._nome = nome
        self._tipo = tipo
        self._saude = saude
    
    def ataque(self):
        print(f"{self._nome} ataca!")

    def esquiva(self):
        print(f"{self._nome} esquiva!")

    def evolui(self):
        print(f"{self._nome} evolui!")


if __name__ == "__main__":
    pikachu = Pokemon("Pikachu", "Elétrico", 60)
    bolbasauro = Pokemon("Bulbasauro", "Planta", 100)

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

        # Abaixo definimos os atributos da classe, assim como os valores que serão inicializados. O python, diferentemente de linguagems como Java e C#, não possui nenhum recurso para indicar se um atributo é privado ou público, nesse caso utilizamos a seguinte padronização: Tudo que começar com um underline ('_') deve ser considerado privado, seja atributo ou método.
        self._nome = nome
        self._tipo = tipo
        self._saude = saude
    
    # Reforçando, todos os métodos de instância deve receber obrigatoriamente o parâmetro self, independentemente se for utilizado ou não
    def ataque(self):
        print(f"{self._nome} ataca!")

    def esquiva(self):
        print(f"{self._nome} esquiva!")

    def evolui(self):
        print(f"{self._nome} evolui!")

    # Podemos utilizar o mesmo padrão de getters e setters de outras linguagens para alterar indiretamente o valor de um atributo privado.
    def set_saude(self, saude: int):
        self._saude = saude

    def get_saude(self) -> int:
        return self._saude
    
    # Ou então utilizar um recurso do Python: a utilização do decorator @property, que faz métodos se comportarem como atributos. Dessa maneira podemos criar um método saude que irá se comportar como um atributo saude
    @property
    def saude(self) -> int:
        return self._saude

    # A partir do atributo criamos o setter
    @saude.setter
    def saude(self, saude):
        self._saude = saude

if __name__ == "__main__":
    # Nas linhas abaixo, estamos instanciando 2 objetos do tipo Pokemon. Os valores que estão sendo passados serão atribuídos aos atributos do objeto no método __init__
    pikachu = Pokemon("Pikachu", "Elétrico", 60)
    bolbasauro = Pokemon("Bulbasauro", "Planta", 100)

    pikachu.evolui()
    print(pikachu.get_saude())
    pikachu.set_saude(20)
    print(pikachu.get_saude())

    # 'saude' é o método da classe Pokemon que agora se comporta como atributo. Dessa maneira não precisamos acessar o atributo privado diretamente.
    pikachu.saude = 30
    print(pikachu.saude)
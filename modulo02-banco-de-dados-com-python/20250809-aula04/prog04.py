"""
Programação Orientada a Objetos

Composição
"""

from random import shuffle
from typing import List

class Carta:

    def __init__(self, naipe: str, valor: str):
        self._naipe = naipe
        self._valor = valor

    # Abaixo utilizamos os métodos mágicos __str__ e __repr__. Métodos mágicos em Python servem tanto para definir comportamentos padrão quando utilizamos recursos/chamadas da linguagem Python para as nossas classes, quanto para adicionar comportamentos nas nossas classes que já existem por padrão no Python
    # Por exemplo, o método mágico __str__ permite que alteremos o comportamento padrão quando passamos a instância da classe para a função built-in str(). No caso abaixo, ao invés de ser mostrado no terminal o padrao '__main__.Carta object at 0x0000089485....', será mostrado o valor e o naipe da carta.
    def __str__(self):
        return f"{self._valor}{self._naipe}"
    
    # O mesmo comportamento de __str__ será utilizado quando utilizamoar a função built-in repr() na instância da classe Carta.
    def __repr__(self):
        return f"{self._valor}{self._naipe}"


class Baralho:

    def __init__(self):
        # atributo privado que irá armazenar a lista de cartas que compõem o baralho
        self._cartas: List[Carta] = []
        self._indice = 0

        # self._valores e self._naipes são listas auxiliares que serão utilizadas na hora da criação do baralho em si.
        self._valores = [
            '2', '3', '4', '5',
            '6', '7', '8', '9',
            '10', 'J', 'Q', 'K',
            'A'
        ]

        self._naipes = [
            '\u2660', '\u2665', '\u2666', '\u2663'
        ]

        # Abaixo o baralho será criado. Para cada naipe e cada valor, será instanciado um objeto do tipo Carta, que será armazenado no atributo privado _cartas.
        for naipe in self._naipes:
            for valor in self._valores:
                self._cartas.append(Carta(naipe=naipe, valor=valor))

        # A função shuffle serve para embaralhar os itens de uma sequência. Nesse caso, a utilizamos para embaralhar as cartas do baralho
        shuffle(self._cartas)

    @property
    def cartas(self):
        return self._cartas
    
    def __str__(self):
        return ' '.join(str(carta) for carta in self._cartas)
    
    def __repr__(self):
        return ' '.join(str(carta) for carta in self._cartas)
    
    # Abaixo utilizamos os métodos __iter__ e __next__ para fazer com que a instância da classe baralho será iterável. Ou seja, podemos utilizar essa instância como o objeto a ser iterado no for loop.
    def __iter__(self):
        return self
    
    def __next__(self):
        # Caso o índice seja maior que o tamanho da lista _cartas, lançamos a exceção StopIteration. O laço for trata essa exceção internamente, portanto o nosso programa não irá ser finalizado. O que é finalizado é o laço for.
        if self._indice > len(self._cartas) - 1:
            raise StopIteration
        
        # A partir do índice atual, pegamos o valor da lista e retornamos.
        item = self._cartas[self._indice]
        self._indice += 1
        return item

if __name__ == "__main__":
    baralho = Baralho()

    for carta in baralho:
        print(carta)

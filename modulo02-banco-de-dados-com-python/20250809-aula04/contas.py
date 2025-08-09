
class ContaFinanceira:

    def __init__(self, nome: str, saldo: float = 0):
        self._nome = nome
        self._saldo = saldo

    @property
    def nome(self) -> str:
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def saldo(self) -> float:
        return self.saldo
    
    def sacar(self, valor: float) -> float:
        if valor > self._saldo:
            raise Exception(f"O valor solicitado (R$ {valor}) é maior que o saldo (R$ {self._saldo}).")
        self._saldo = self._saldo - valor
        return valor
    
    def depositar(self, valor: float):
        if valor <= 0:
            raise Exception("O valor a ser depositado deve ser maior do que 0.")
        self._saldo = self._saldo + valor


class ContaCorrente(ContaFinanceira):
    pass

class ContaInvestimento(ContaFinanceira):

    def __init__(self, nome: str, saldo: float = 0, taxa: float = 0.01):
        super().__init__(nome, saldo)
        self._taxa = taxa

    def render(self) -> float:
        rendimento = (self._saldo * self._taxa)
        self._saldo = self._saldo + rendimento

        return rendimento
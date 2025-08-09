
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
        return self._saldo
    
    def sacar(self, valor: float) -> float:
        # Abaixo temos uma verificação do valor passado para saque. Se o valor por maior que o saldo atual da conta, será gerada uma exceção. Uma exceção, quando lançada, interrompe imediatamente a execução do programa, caso ela não seja capturada e tratada.
        # Podemos gerar exceções no nosso programa para comportamentos inesperados (como um erro de comunicação com uma API, por exemplo) ou até mesmo fazendo parte da regra de negócio. Abaixo nosso programa irá finalizar caso o valor seja maior que o saldo.
        if valor > self._saldo:
            raise Exception(f"O valor solicitado (R$ {valor}) é maior que o saldo (R$ {self._saldo}).")
        self._saldo = self._saldo - valor
        return valor
    
    def depositar(self, valor: float):
        if valor <= 0:
            raise Exception("O valor a ser depositado deve ser maior do que 0.")
        self._saldo = self._saldo + valor


# A sintaxe abaixo corresponde a implementação da herança. Nesse caso, criamos a classe ContaCorrente que herda os atributos e métodos da classe ContaFinanceira. Como não implementamos nada a mais na classe ContaCorrente, ela terá exatamente os mesmos métodos e atributos da classe ContaFinanceira.
class ContaCorrente(ContaFinanceira):
    pass

class ContaInvestimento(ContaFinanceira):

    # Aqui estamos criando o método __init__ da classe ContaInvestimento. Nesse caso, esse método está sobrescrevendo o método __init__ que está sendo herdado da classe ContaFinanceira. Podemos fazer isso sem problemas com quaisquer métodos que estiverem sendo herdados.
    def __init__(self, nome: str, saldo: float = 0, taxa: float = 0.01):

        # Como estamos sobrescrevendo o método __init__, o código da do método da classe mãe está sendo substituído. Porém, podemos chamar o método que está sendo substituído se quisermos reusar a implementação. Nesse caso utilizamos a função built-in super(), que chama qualquer método da classe mãe.
        # No caso abaixo, estamos reutilizando o método __init__ de ContaFinanceira para definir os valores dos atributos herdados _nome e _saldo, enquanto criamos um novo atributo para a nossa classe ContaInvestimento chamado _taxa. Reutilização de código é uma das principais vantagens que temos quando utilizamos orientação a objetos.
        super().__init__(nome, saldo)
        self._taxa = taxa

    # Além dos métodos sacar() e depositar() que já estamos herdando da classe ContaFinanceira, criamos também o método render, que irá aumentar o saldo da conta a partir do rendimento.
    def render(self) -> float:
        rendimento = (self._saldo * self._taxa)
        self._saldo = self._saldo + rendimento

        return rendimento
    

# Por fim, criamos a classe ContaPoupancaCaixa, que irá herdar todos os atributos e métodos da classe ContaInvestimento e de quaisquer classes que ContaInvestimento estiver herdando.
class ContaPoupancaCaixa(ContaInvestimento):

    def __init__(self, saldo = 0, taxa = 0.01):
        super().__init__("Conta Poupança Caixa", saldo, taxa)

# https://speakerdeck.com/curiouslearner/method-resolution-order-in-python
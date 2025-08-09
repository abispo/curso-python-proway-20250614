"""
Programação Orientada a Objetos

Polimorfismo
"""

from typing import List

class Funcionario:

    def __init__(self, nome: str):
        self._nome = nome

    @property
    def nome(self) -> str:
        return self._nome
    
    def calcular(self):
        raise NotImplementedError
    

class FuncionarioCLT(Funcionario):

    def __init__(self, nome: str, salario: float):
        super().__init__(nome)
        self._salario = salario

    def calcular(self) -> float:
        return self._salario
    

class FuncionarioTerceirizado(Funcionario):

    def __init__(self, nome: str, preco_hora: float, quantidade_horas: int):
        super().__init__(nome)
        self._preco_hora = preco_hora
        self._quantidade_horas = quantidade_horas

    def calcular(self) -> float:
        return self._preco_hora * self._quantidade_horas
    

class FuncionarioComissionado(Funcionario):

    def __init__(self, nome: str, valor_total_vendas: float, porcentagem_comissao: float):
        super().__init__(nome)
        self._valor_total_vendas = valor_total_vendas
        self._porcentagem_comissao = porcentagem_comissao

    def calcular(self) -> float:
        return self._valor_total_vendas * (self._porcentagem_comissao / 100)
    

class FolhaDePagamento:

    def __init__(self, funcionarios: List[Funcionario]):
        self._funcionarios = funcionarios

    def gerar(self):
        print(" ===== GERAÇÃO DE FOLHA DE PAGAMENTO =====")
        for funcionario in self._funcionarios:
            nome = funcionario.nome
            tipo = funcionario.__class__.__name__
            salario = funcionario.calcular()

            print(" = Dados do Funcionário")
            print(f" = Nome: {nome}")
            print(f" = Tipo: {tipo}")
            print(f" = Salário: {salario:.2f}")
            print('*'*30)
        print(" ================================== ")
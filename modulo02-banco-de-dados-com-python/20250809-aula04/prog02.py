"""
Programação Orientada a Objetos

Herança
"""

from contas import ContaCorrente, ContaInvestimento, ContaPoupancaCaixa

if __name__ == "__main__":

    cc_viacredi = ContaCorrente("Conta Corrente Viacredi")
    cp_caixa = ContaInvestimento("Conta Poupança Caixa", 150)

    cc_viacredi.depositar(100)
    cc_viacredi.sacar(80)
    print(f"Saldo de '{cc_viacredi.nome}': {cc_viacredi.saldo}.")

    rendimento = cp_caixa.render()
    print(f"'{cp_caixa.nome}' rendeu R${rendimento}.")

    cp_caixa.depositar(100)
    cp_caixa.sacar(80)
    print(f"Saldo de '{cp_caixa.nome}': {cp_caixa.saldo}.")

    cp_caixa2 = ContaPoupancaCaixa(1000, 0.05)
    cp_caixa2.render()
    print(cp_caixa2.saldo)
"""
Laços de condição em Python

match case

A partir da versão 3.10 do Python, podemos utilizar outro laço de condição do Python: o match. Ele funciona exatamente como o switch case de linguagens como Java e C#. Utilizamos o match case nos casos onde temos mais controle dos resultados possíveis de uma comparação.
"""

if __name__ == "__main__":

    comando = input("Informe o comando que deseja executar: ").upper()

    match comando:
        case "INICIAR":
            print("O processo foi iniciado.")

        case "INTERROMPER":
            print("O processo foi interrompido.")

        case "FINALIZAR":
            print("O processo foi finalizado.")

        case _:
            print(f"Comando '{comando}' desconhecido.")

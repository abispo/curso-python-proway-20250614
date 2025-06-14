# Comentários em Python começão com o caractere '#'

# Apesar de não ser obrigatório, é uma boa prática colocar a condição abaixo em todo script que for executado diretamente pelo interpretador Python. É como se fosse o método main de linguagens como Java ou C#. Abaixo estamos verificando se a variável __name__ possui o valor igual a "__main__". Para isso, utilizamos a estrutura de condição if
if __name__ == "__main__":

    # Sempre que uma linha termina com 2 pontos, como está acima, um novo bloco de código é criado. Obrigatoriamente, esse bloco deve ter um espaçamento de no mínimo 1 caractere, com o padrão sendo de 4 caracteres. Todas as linhas desse bloco de código devem seguir o mesmo espaçamento. Geralmente a própria IDE cuida desses detalhes.

    # A linha abaixo atribui o valor de retorno da função built-in input() a variável nome. As funções built-in são funções que são carregadas automaticamente quando executamos o interpretador Python.
    # No caso da função input, ela retorna o valor que foi digitado pelo terminal no formato string(texto). Utilizamos o operador de atribuição = (igual a) para salvar esse valor na variável nome. Como o Python é uma linguagem de tipagem dinâmica, o tipo dessa variável será definido automaticamente em tempo de execução, não sendo obrigatório indicarmos o tipo da variável, como estamos fazendo abaixo (apesar de ser uma boa prática).
    # https://www.w3schools.com/python/python_ref_functions.asp
    nome: str = input("Informe o seu nome: ")

    # Abaixo, estamos concatenando o nome recebido via terminal com outra string. Para isso, utilizamos o padrão f-string, onde a expressão dentro das chaves retornará um valor.
    print(f"Olá {nome}, bem-vindo(a) ao curso de Python.")

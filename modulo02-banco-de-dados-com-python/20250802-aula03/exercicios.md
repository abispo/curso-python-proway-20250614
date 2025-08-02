# Exercícios Formas Normais

# Normalize (aplique as formas normais que achar necessário) as tabelas abaixo.

```
PS: As colunas que contém asterisco (*) são as chaves primárias das tabelas
```

#### tb_pedidos

| \*pedido_id | data_hora           | nome_cliente | produto                 | quantidade |
| ----------- | ------------------- | ------------ | ----------------------- | ---------- |
| 1           | 2025-05-12 04:05:10 | João Silva   | Camisa, Caneca          | 2, 1       |
| 2           | 2025-05-12 04:05:10 | Jane Smith   | Adesivo, Caneca, Cantil | 1, 3, 2    |
| 3           | 2025-05-12 04:05:10 | Sara Correa  | Cafeteira               | 1          |

---

#### tb_funcionarios

| \*funcionario_id | nome        | endereco                              | habilidades                   |
| ---------------- | ----------- | ------------------------------------- | ----------------------------- |
| 1                | John Smith  | Praça da Sé, 1000, São Paulo, SP      | HTML, CSS, JavaScript, Python |
| 2                | Jane Doe    | Rua 7 de Setembro, 1500, Blumenau, SC | HTML, CSS, SQL                |
| 3                | Bob Johnson | Rua 15 de Novembro, 56, Blumenau, SC  | Python, Java                  |

---

#### tb_filmes

| nome_filme   | ano_lancamento | diretor          | ator_1            | ator_2       | ator_3           |
| ------------ | -------------- | ---------------- | ----------------- | ------------ | ---------------- |
| Tubarão      | 1975           | Steven Spielberg | Roy Scheider      | Robert Shaw  | Richard Dreyfuss |
| Titanic      | 1997           | James Cameron    | Leonardo DiCaprio | Kate Winslet | Billy Zane       |
| Forrest Gump | 1994           | Robert Zemeckis  | Tom Hanks         | Robin Wright | Gary Sinise      |

---

| \*Código Disciplina | Nome Disciplina | Departamento | Nome Professor | \*Código Aluno | Nome Aluno  | Nota |
| ------------------- | --------------- | ------------ | -------------- | -------------- | ----------- | ---- |
| 1001                | Cálculo I       | Matemática   | Ana Souza      | 001            | João Silva  | 8.0  |
| 1001                | Cálculo I       | Matemática   | Ana Souza      | 002            | Ana Santos  | 6.5  |
| 1002                | Programação I   | Computação   | Pedro Silva    | 002            | Ana Santos  | 9.0  |
| 1002                | Programação I   | Computação   | Pedro Silva    | 003            | Carlos Lima | 7.5  |

---

| Disciplina       | Aluno           | Nota 1 | Nota 2 | Nota 3 | Média |
| ---------------- | --------------- | ------ | ------ | ------ | ----- |
| Estatística      | João Silva      | 8.5    | 9.0    | 8.5    | 8.6   |
| Matemática       | Maiara Nogueira | 10.0   | 9.5    | 9.5    | 9.6   |
| Java             | Danielle Souza  | 7.5    | 7.5    | 7.0    | 7.3   |
| Ciência de Dados | José Duarte     | 6.5    | 5.5    | 7.5    | 6.5   |

---

| \*ID | \*ID Servico | Total de Horas | Valor Hora | Subtotal |
| ---- | ------------ | -------------- | ---------- | -------- |
| 0001 | 0001         | 40             | 10         | 400      |
| 0002 | 0002         | 12             | 40         | 480      |
| 0003 | 0002         | 10             | 40         | 400      |
| 0004 | 0003         | 30             | 20         | 600      |

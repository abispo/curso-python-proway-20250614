/*
Primeira Forma Normal (1FN)

Precisamos seguir algumas regras para garantir que uma tabela esteja de acordo
com as formas normais. No caso da 1FN, as seguintes regras devem ser seguidas:

- Cada coluna da tabela deve ter apenas valores atômicos ou indivisíveis, ou seja,
não pode ter valores compostos
- Não podemos ter na tabela colunas multivaloradas, ou seja, uma coluna com mais
de 1 valor
- Ter uma  ou mais colunas identificando cada registro, sendo fortemente
recomendável a criação de uma chave primária.
*/

CREATE DATABASE IF NOT EXISTS modulo02_nfs;

-- Criação da tabela tb_clientes, que não está normalizada

CREATE TABLE IF NOT EXISTS tb_clientes(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(100) NOT NULL,
	endereco VARCHAR(200) NOT NULL,
	telefone VARCHAR(50) NOT NULL
);

INSERT INTO tb_clientes (nome, endereco, telefone) VALUES (
	'Maria das Dores',
	'Rua XV de Novembro, 100, Centro, Blumenau, SC',
	'47933333333'
);
INSERT INTO tb_clientes(nome, endereco, telefone) VALUES (
	'João da Silva',
	'Praça da Liberdade, 12, Liberdade, São Paulo, SP',
	'11988888888,47977777777'
);
INSERT INTO tb_clientes(nome, endereco, telefone) VALUES (
	'Carlos Manuel Carvalho',
	'Rua dos Bandeirantes, 240, Centro, Pomerode, SC',
	'47955555555'
);
SELECT * FROM tb_clientes;

/*
No caso da tabela tb_clientes, a coluna endereço é uma coluna que armazena
valores compostos (um endereço é composto de logradouro, numero, bairro, etc).
A coluna telefone possui registros onde mais de 1 telefone está salvo. Essas
duas características violam a 1FN. Vamos criar uma tabela respeitando essas
regras:
*/

ALTER TABLE tb_clientes RENAME TO tb_clientes_pre_1fn;

CREATE TABLE IF NOT EXISTS tb_clientes(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(100) NOT NULL,
	tipo_logradouro VARCHAR(20) NOT NULL,
	logradouro VARCHAR(50) NOT NULL,
	numero VARCHAR(10) NOT NULL,
	bairro VARCHAR(50) NOT NULL,
	cidade VARCHAR(50) NOT NULL,
	uf CHAR(2) NOT NULL
);

INSERT INTO tb_clientes (
	nome, tipo_logradouro, logradouro, numero, bairro, cidade, uf
) VALUES
	(
	'Maria das Dores',
	'Rua', 'XV de Novembro', '100', 'Centro', 'Blumenau', 'SC'
	),
	(
	'João da Silva',
	'Praça', 'da Liberdade', '12', 'Liberdade', 'São Paulo', 'SP'
	),
	(
	'Carlos Manuel Carvalho',
	'Rua', 'dos Bandeirantes', '240', 'Centro', 'Pomerode', 'SC'
	);
SELECT * FROM tb_clientes;

/*
No caso da coluna telefone, como é uma coluna que pode ter dados multivalorados,
a saída é criar uma tabela que irá armazenar esses telefones. Essa tabela será
relacionada com a tabela de clientes.
*/

CREATE TABLE IF NOT EXISTS tb_telefones(
	id INT PRIMARY KEY AUTO_INCREMENT,
	cliente_id INT NOT NULL,
	ddd TINYINT UNSIGNED NOT NULL,
	telefone VARCHAR(20) NOT NULL
);

ALTER TABLE tb_telefones ADD FOREIGN KEY(cliente_id) REFERENCES tb_clientes(id);

INSERT INTO tb_telefones(cliente_id, ddd, telefone) VALUES
	(1, 47, '933333333'),
	(2, 11, '988888888'),
	(2, 47, '977777777'),
	(3, 47, '955555555');

INSERT INTO tb_clientes(
	nome, tipo_logradouro, logradouro, numero, bairro, cidade, uf
) VALUES (
	'Barbara dos Santos',
	'Avenida',
	'Brasil',
	'1500',
	'Centro',
	'Rio de Janeiro',
	'RJ'
);

SELECT tc.nome, tt.ddd, tt.telefone FROM tb_clientes tc
INNER JOIN tb_telefones tt
ON tc.id = tt.cliente_id;

/*
Terceira Forma Normal (3FN)

Para uma tabela estar na 3FN, é necessário que:
- Ela esteja na 2FN
- Todas as colunas não chave da tabela não podem depender de outras colunas
não chave. Chamamos esse dependência de dependência transitiva.
*/

CREATE DATABASE IF NOT EXISTS modulo02_fns;

-- Criação da tabela de produtos
CREATE TABLE IF NOT EXISTS tb_produtos(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(100) NOT NULL,
	valor_unitario FLOAT NOT NULL
);
INSERT INTO tb_produtos(nome, valor_unitario) VALUES
	('Morango do Amor', 20),
	('Labubu', 80),
	('Mochila do Naruto', 100),
	('Copo térmico', 50),
	('Perfume árabe', 300);
SELECT * FROM tb_produtos;

-- Criação da tabela de pedidos
CREATE TABLE IF NOT EXISTS tb_pedidos(
	id INT PRIMARY KEY AUTO_INCREMENT,
	data_hora DATETIME NOT NULL,
	observacoes VARCHAR(100) NOT NULL
);
INSERT INTO tb_pedidos(data_hora, observacoes) VALUES
	('2025-05-01 14:55:21', 'Produtos da moda'),
	('2025-05-01 14:49:33', 'Primeira compra'),
	('2025-05-02 01:45:10', 'Itens para viagem');
SELECT * FROM tb_pedidos;

-- Criação da tabela associativa entre produtos e pedidos
CREATE TABLE IF NOT EXISTS tb_produtos_pedidos(
	pedido_id INT NOT NULL,
	produto_id INT NOT NULL,
	quantidade INT NOT NULL,
	subtotal FLOAT NOT NULL,
	PRIMARY KEY(pedido_id, produto_id),
	FOREIGN KEY(pedido_id) REFERENCES tb_pedidos(id),
	FOREIGN KEY(produto_id) REFERENCES tb_produtos(id));

INSERT INTO tb_produtos_pedidos(pedido_id, produto_id, quantidade, subtotal) VALUES
	(1, 1, 2, 40),
	(1, 2, 1, 80),
	(1, 5, 1, 300),
	(2, 5, 2, 600),
	(3, 3, 1, 100),
	(3, 4, 3, 150);
SELECT * FROM tb_produtos_pedidos;

SELECT tpi.id AS 'Id do Pedido',
		tpi.data_hora AS 'Data/Hora do Pedido',
		tpo.id AS 'Id do Produto',
		tpo.nome AS 'Nome do Produto',
		tpo.valor_unitario AS 'Valor Unitário',
		tpp.quantidade AS 'Quantidade',
		-- tpp.subtotal AS 'Subtotal'    -- Coluna removida para 3FN
		tpo.valor_unitario * tpp.quantidade AS 'Subtotal'
FROM tb_pedidos tpi
INNER JOIN tb_produtos_pedidos tpp
ON tpi.id = tpp.pedido_id
INNER JOIN tb_produtos tpo
ON tpp.produto_id = tpo.id
ORDER BY tpi.data_hora;

/*
 A consulta acima trás os dados de pedidos, assim como de produtos. A coluna
 subtotal depende de 2 colunas que não são chave primária: valor_unitario da
 tabela de produtos e quantidade da tabela de produtos_pedidos. Nesse caso existe
 a violaçao da 3FN. Para resolver isso, simplesmente removemos a coluna
 subtotal da tabela de produtos_pedidos, e calculamos o valor na própria consulta,
 multiplicando o valor_unitario do produto pela quantidade. Dessa maneira a coluna
 irá existir apenas na execução da consulta.
 */

ALTER TABLE tb_produtos_pedidos DROP COLUMN subtotal;
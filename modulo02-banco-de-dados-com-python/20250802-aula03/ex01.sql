
-- Exercícios aula 03 módulo 02 Python com banco de dados

-- 01
CREATE DATABASE IF NOT EXISTS modulo02_aula03_exercicios;
USE modulo02_aula03_exercicios;

CREATE TABLE IF NOT EXISTS tb_produtos(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(100) NOT NULL,
	valor_unitario FLOAT NOT NULL
);
INSERT INTO tb_produtos (nome, valor_unitario) VALUES
	('Camisa', 10),
	('Caneca', 25),
	('Adesivo', 5.90),
	('Cantil', 19.90),
	('Cafeteira', 220.70);
SELECT * FROM tb_produtos;

CREATE TABLE IF NOT EXISTS tb_clientes(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(100) NOT NULL
);
INSERT INTO tb_clientes(nome) VALUES
	('João Silva'),
	('Jane Smith'),
	('Sara Correa');
SELECT * FROM tb_clientes;

CREATE TABLE IF NOT EXISTS tb_pedidos(
	id INT PRIMARY KEY AUTO_INCREMENT,
	cliente_id INT NOT NULL,
	data_hora DATETIME NOT NULL,
	FOREIGN KEY(cliente_id) REFERENCES tb_clientes(id)
);
INSERT INTO tb_pedidos(cliente_id, data_hora) VALUES
	(1, '2025-05-06 13:56:55'),
	(2, '2025-05-08 19:42:32'),
	(3, '2025-05-08 17:36:22');
SELECT * FROM tb_pedidos;

CREATE TABLE IF NOT EXISTS tb_pedidos_produtos(
	pedido_id INT NOT NULL,
	produto_id INT NOT NULL,
	quantidade INT NOT NULL,
	PRIMARY KEY(pedido_id, produto_id),
	FOREIGN KEY(pedido_id) REFERENCES tb_pedidos(id),
	FOREIGN KEY(produto_id) REFERENCES tb_produtos(id)
);
INSERT INTO tb_pedidos_produtos(pedido_id, produto_id, quantidade) VALUES
	(1, 1, 2),
	(1, 2, 1),
	(2, 3, 1),
	(2, 2, 3),
	(2, 4, 2),
	(3, 5, 1);
SELECT * FROM tb_pedidos_produtos;
-- --------------------------------------------------------------------
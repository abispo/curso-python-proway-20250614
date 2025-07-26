/*

Relacionamento entre tabelas em um banco de dados.

Um banco de dados relacional possui esse nome pois permite criar relaciomentos
entre as suas entidades, que podemos chamar de tabelas. Dentro de um banco de
dados relacional, podemos ter 3 níveis de relacionamento entre tabelas:

1:1 -> Um para um
1:N -> Um para muitos
N:N -> Muitos para muitos.

Entender como as tabelas se relacionam é um passo fundamental na fase de
modelagem de dados da nossa aplicação. Relacionamentos mal definidos podem levar
a perda de consistência e confiabilidade dos dados.

Para ilustrar os níveis de relacionamento, vamos montar a estrutura de banco de
dados de uma aplicação de blog, onde o usuário pode criar postagens, comentários,
etc.

Nesse caso, nosso sistema terá 5 entidades (tabelas):
* Tabela para os Usuarios
* Tabela para os Perfis
* Tabela para as Postagens
* Tabela para as Categorias
* Tabela para os Comentários

* No caso dos dados do usuário, separamos em 2 tabelas: Uma para os dados de
acesso (email, senha, etc) e outra para os dados pessoais (nome, genero, etc)
*/

CREATE DATABASE IF NOT EXISTS relacionamentos;

CREATE TABLE IF NOT EXISTS usuarios(
	id INT PRIMARY KEY AUTO_INCREMENT,
	email VARCHAR(100) NOT NULL,
	senha VARCHAR(100) NOT NULL,
	criado_em DATETIME DEFAULT CURRENT_TIMESTAMP()
);
SELECT * FROM usuarios;

CREATE TABLE IF NOT EXISTS perfis(
	id INT PRIMARY KEY,
	nome VARCHAR(100) NOT NULL,
	data_de_nascimento DATE NULL,
	genero VARCHAR(50) NULL
-- 	FOREIGN KEY(id) REFERENCES usuarios(id)
);

-- Caso você queira adicionar a chave estrangeira depois
ALTER TABLE perfis ADD FOREIGN KEY(id) REFERENCES usuarios(id);

/*
Acima, criamos um relacionamento entre as tabelas usuarios e perfis. Utilizamos
a instrução FOREIGN KEY... REFERENCES para criar essa ligação. Como criamos
essa ligação na coluna id de perfis, que também é chave primária, os valores
dessa coluna ao mesmo tempo que não devem se repetir, devem existir na tabela
usuarios (tabela referenciada). Abaixo veremos alguns exemplos.
*/

INSERT INTO usuarios(email, senha) VALUES (
	'joao.silva@email.com', 'joao123'
);
INSERT INTO usuarios(email, senha) VALUES ( 
	'maria.batista@email.com', 'maria123'
);
INSERT INTO usuarios(email, senha) VALUES (
	'barbara.barreto@email.com', 'barbara123'
);
SELECT * FROM usuarios;

INSERT INTO perfis(id, nome, data_de_nascimento, genero) VALUES (
	1, 'João da Silva', '1980-11-17', 'Masculino'
);
INSERT INTO perfis(id, nome, data_de_nascimento, genero) VALUES (
	2, 'Maria Batista', NULL, 'Feminino'
);
SELECT * FROM perfis;

/*
Acima garantimos a aplicação do relacionamento 1:1, garantindo que não haverá
valores repetidos para as colunas id das tabelas usuarios e perfis, e garantindo
que os valores da coluna id da tabela perfis existem na tabela usuarios
*/


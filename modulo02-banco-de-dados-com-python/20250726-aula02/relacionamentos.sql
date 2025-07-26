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

CREATE TABLE IF NOT EXISTS perfis(
	id INT PRIMARY KEY,
	nome VARCHAR(100) NOT NULL,
	data_de_nascimento DATE NULL,
	genero VARCHAR(50) NULL
-- 	FOREIGN KEY(id) REFERENCES usuarios(id)
);

-- Caso você queira adicionar a chave estrangeira depois
ALTER TABLE perfis ADD FOREIGN KEY(id) REFERENCES usuarios(id);
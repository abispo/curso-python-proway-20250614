/*
Segunda Forma Normal (2FN)

Uma tabela está na 2FN, quando:
- Ela está na 1FN
- Todas as colunas não-chave da tabela dependem inteiramente de todas as partes
da chave primária. Chamamos isso de dependência funcional total
*/

CREATE DATABASE IF NOT EXISTS modulo02_fns;

-- A tabela abaixo viola as regras da 2FN
CREATE TABLE IF NOT EXISTS tb_matriculas(
	curso_id INT NOT NULL,
	aluno_id INT NOT NULL,
	nome_curso VARCHAR(100) NOT NULL,
	nome_aluno VARCHAR(100) NOT NULL,
	carga_horaria INT NOT NULL
);

ALTER TABLE tb_matriculas ADD PRIMARY KEY(curso_id, aluno_id);

INSERT INTO tb_matriculas(
	curso_id, aluno_id, nome_curso, nome_aluno, carga_horaria
) VALUES
	(1, 1, 'Montagem e Manutenção de PCs', 'Andressa Motta', 40),
	(1, 2, 'Montagem e Manutenção de PCs', 'Daniel Silva', 36),
	(2, 3, 'Programação Python Básica', 'Daniel Silva', 60),
	(3, 1, 'Java Avançado', 'Marcos Oliveira', 35),
	(1, 5, 'Banco de Dados', 'Barbara Garcia', 40);
SELECT * FROM tb_matriculas t ;

/*
Na tabela acima, temos as colunas não-chave nome_curso, nome_aluno e carga_horaria.
nome_curso e carga_horaria existem em função de curso_id (coluna identificadora),
enquanto nome_aluno existe em função de aluno_id. Ou seja, temos colunas que
dependem apenas de parte da chave primária, e não do seu todo. Por esse motivo
temos algumas inconsistências nos registros, como alunos de mesmo id porém
nomes diferentes, cursos de mesmo id com nomes e cargas horárias diferentes, etc.

Nesse caso, temos que separar os domínios em tabelas diferentes. E também vamos
criar uma coluna que depende de todas as partes da chave primária.
*/

ALTER TABLE tb_matriculas RENAME TO tb_matriculas_pre_2fn;

CREATE TABLE IF NOT EXISTS tb_cursos(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(100) NOT NULL,
	carga_horaria SMALLINT unsigned
);
INSERT INTO tb_cursos (nome, carga_horaria) VALUES
	('Montagem e Manutenção de PCs', 40),
	('Programação Python Básica', 20),
	('Java Avançado', 50),
	('Banco de Dados', 40),
	('Automação com Arduino', 120);
SELECT * FROM tb_cursos;

/*
Acima foi criada a tabela tb_cursos, que irá armazenar todos os dados referentes ao curso.
Perceba que todas as colunas dessa tabela (nome, carga_horaria) dependem da chave
primária da tabela (id).
*/

CREATE TABLE IF NOT EXISTS tb_alunos(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(100) NOT NULL
);
INSERT INTO tb_alunos (nome) VALUES
	('Andressa Motta'),
	('Daniel Silva'),
	('Marcos Oliveira'),
	('Barbara Garcia');
SELECT * FROM tb_alunos;

/*
Fizemos a mesma coisa com alunos: Separamos os dados de alunos em uma tabela, que assim
como cursos, vamos referenciar na tabela tb_matriculas
*/

CREATE TABLE IF NOT EXISTS tb_matriculas(
	curso_id INT NOT NULL,
	aluno_id INT NOT NULL,
	data_matricula DATE NOT NULL,
	PRIMARY KEY(curso_id, aluno_id),
	FOREIGN KEY(curso_id) REFERENCES tb_cursos(id),
	FOREIGN KEY(aluno_id) REFERENCES tb_alunos(id)
);

INSERT INTO tb_matriculas(curso_id, aluno_id, data_matricula) VALUES
	(1, 1, '2025-02-24'),
	(1, 2, '2025-03-01'),
	(2, 3, '2025-03-01'),
	(3, 1, '2025-04-15'),
	(1, 4, '2025-02-25');

SELECT * FROM tb_matriculas;

SELECT ta.nome, tc.nome, tc.carga_horaria, tm.data_matricula FROM tb_alunos ta
INNER JOIN tb_matriculas tm
ON ta.id = tm.aluno_id
INNER JOIN tb_cursos tc
ON tm.curso_id = tc.id
ORDER BY tc.id;

/*
Com isso, a nossa tabela de matriculas irá apenas referencias os cursos e os alunos
pela sua coluna identificadora (id). Também criamos a coluna data_matrícula, que indica
quando um determinado aluno fez a matrícula em um curso. Ou seja, essa coluna depende
de todas as partes da chave primária (dependência funcional total)
*/
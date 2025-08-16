# Introdução ao SQLAlchemy

**SQLAlchemy** é uma biblioteca de código aberto em Python que atua como um "tradutor" entre o seu código e o banco de dados. Em vez de escrever código SQL complexo, você pode interagir com o banco de dados usando a sintaxe de objetos Python, o que torna o desenvolvimento mais rápido e intuitivo.

---

### O que é um ORM?

**ORM** significa *Object-Relational Mapper* (Mapeador Objeto-Relacional). A sua função é mapear objetos da sua linguagem de programação para tabelas em um banco de dados relacional.

Basicamente, um ORM permite que você trabalhe com os dados do seu banco de dados como se eles fossem objetos Python. Por exemplo, em vez de escrever uma consulta SQL para buscar dados de um usuário, você pode simplesmente usar `usuario.nome` ou `usuario.email` para acessar as informações, o que simplifica bastante o seu trabalho.

O SQLAlchemy possui uma das implementações de ORM mais poderosas e populares, além de uma ferramenta para construir consultas SQL de forma mais programática, o **SQLAlchemy Core**.


### Desafio
Você ira criar a model `Post`, que irá representar a tabela `posts` no banco de dados. Essa tabela irá armazenar as postagens feitas pelos usuários, e terá uma relação de N:1 para a tabela User. A tabela deve ter a seguinte estrutura:

* Coluna `id`, int, chave primária e auto incremento
* Coluna user_id, int, chave estrangeira da tabela users (coluna id)
* Coluna titulo, varchar(100), não pode conter valores nulos
* Coluna content, varchar(1000), não pode conter valores nulos

* Na model Post criar a propriedade user, que será do tipo relationship e trará a instância de User que criou essa postagem.
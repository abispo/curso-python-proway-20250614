# Módulo 6: Migrações de Banco de Dados com Alembic

Neste último módulo, exploraremos o **Alembic**, uma ferramenta essencial para gerenciar as **migrações de schema** do seu banco de dados.

Quando desenvolvemos uma aplicação, o modelo de dados (o schema do banco) está em constante evolução. Adicionar uma nova coluna, alterar um tipo de dado ou remover uma tabela são ações comuns. O Alembic resolve o desafio de manter o seu banco de dados e o seu código em sincronia, garantindo que as alterações no schema sejam aplicadas de forma controlada e segura.

---

### O que é Alembic?

**Alembic** é uma ferramenta de **versionamento de banco de dados** que permite realizar alterações na estrutura do banco utilizando apenas código, por meio de arquivos chamados de **`migrations`**. Quando trabalhamos com ORMs (Object-Relational Mappers), essa é a maneira comum e recomendada de lidar com alterações na estrutura das tabelas.

### Vantagens do Versionamento de Banco de Dados com Alembic

- **Controle de Versão:** As migrações são scripts que descrevem as alterações no seu banco de dados. Ao usá-las, você tem um histórico completo de todas as modificações do schema, permitindo que você navegue entre versões de forma fácil e segura, assim como você faz com o código da sua aplicação em ferramentas como o Git.

- **Colaboração Simplificada:** Em projetos de equipe, cada desenvolvedor pode estar trabalhando em uma alteração diferente no banco de dados. O Alembic garante que as migrações sejam aplicadas na ordem correta, evitando conflitos e garantindo que o ambiente de desenvolvimento de todos esteja sempre atualizado com a versão mais recente do schema.

- **Ambientes Sincronizados:** Mover a aplicação do ambiente de desenvolvimento para o de produção (ou qualquer outro ambiente) se torna um processo previsível. Em vez de executar comandos SQL manualmente, você simplesmente aplica as migrações pendentes, garantindo que todos os ambientes tenham o mesmo schema.

- **Redução de Erros:** O Alembic utiliza scripts Python para realizar as alterações, o que permite automatizar e testar o processo. Ele também oferece a capacidade de **reverter** (downgrade) uma migração, caso algo dê errado, proporcionando uma camada de segurança extra.

- **Integração com SQLAlchemy:** O Alembic foi desenvolvido para ser usado com o **SQLAlchemy**, a ORM mais popular do ecossistema Python. A ferramenta consegue detectar automaticamente as diferenças entre os modelos de dados do seu código e o schema do banco, facilitando a geração de novas migrações.

---

### Instalação e Uso

Para começar, a instalação é simples:

```bash
pip install alembic
```

Depois, você precisa inicializar a estrutura de pastas do Alembic com o comando:

```bash
alembic init alembic
```

Isso criará a pasta `alembic` no diretório raiz do seu projeto, contendo a seguinte estrutura:

- `alembic.ini`: Armazena as configurações globais do Alembic.
- `alembic/env.py`: Arquivo principal para a execução de comandos. A partir dele, você pode personalizar as configurações.
- `alembic/script.py`.mako: O template usado para gerar novos arquivos de migração.
- `alembic/versions/`: O diretório onde todas as suas migrações serão salvas.

Após alterar um modelo (uma classe que representa uma tabela no seu banco), você gera uma nova migração com o comando:

```bash
alembic revision --autogenerate --message "[mensagem]"
```

Esse comando irá comparar o seu modelo de dados com a estrutura atual do banco e, se houver diferenças, criará um novo arquivo de migração no diretório `alembic/versions/`. O nome do arquivo será uma combinação de um código aleatório com a mensagem que você forneceu.

Finalmente, para aplicar as alterações ao seu banco de dados, você usa o comando:

```bash
alembic upgrade head
```

Isso aplica a migração mais recente que ainda não foi executada no banco.

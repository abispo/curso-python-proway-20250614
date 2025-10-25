# Criação das páginas de listagem de tickets, criação e edição de ticket

Você deve criar os templates, as funções view e as rotas para as funcionalidades de ticket. Lembrando que todas essas rotas devem ser acessadas apenas por usuários logados. As rotas devem ser as seguintes:

* `/tickets`: É a rota onde serão listados todos os tickets abertos pelo usuário atual.
* `/tickets/new`: É a rota onde o usuário irá abrir um novo ticket
* `/tickets/{id}`: É a rota onde o usuário irá visualizar o ticket aberto e poderá editá-lo

Nessas páginas, os únicos campos que estarão disponíveis para o usuário alterar serão o título do ticket e a descrição. O owner deve ser preenchido com o usuário atualmente logado e o campo status deve ter o valor "open".

Os nomes dos templates e das funções view devem fazer sentido com cada funcionalidade (listar, criar e editar).
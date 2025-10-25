# Criação da página de perfil do usuário.

Logo após se logar, o usuário poderá acessar a sua página de perfil a partir de um link. Nessa página, ele poderá alterar algumas informações, nesse momento serão: Nome, sobrenome e data de nascimento. A rota para o perfil do usuário será `users/me/profile`.

Nessa página, as informações do usuário serão mostradas em um formulário. Esse formulário terá 3 campos: Um para cada informação a ser alterada. É importante frizar que os dados atuais do usuário serão carregados nesses campos Caso o usuário clique no botão "Atualizar", as informações do perfil do usuário serão atualizadas e o usuário será redirecionado para a rota `users/me`. Os dados desse formulário serão enviados para a mesma rota `/users/me/profile`.

O nome do template que será mostrado, será `users/profile.html`. A rota que será chamada é `users/me/profile`, e a função view que será chamada a partir da rota se chamará `profile`. A criação do formulário fica a sua escolha: Pode ser criado inteiramente no template, ou criado a partir de uma classe `Form` do Django e renderizado.
from django import forms
from django.shortcuts import render

from .forms import PreRegisterForm
from .validators import email_already_exists_in_users, email_alreads_exists_in_pre_register

def pre_register(request):

    if request.method == "GET":

        form = PreRegisterForm()

        return render(
            request,
            "register/pre_register.html",
            {"form": form}
        )
    
    elif request.method == "POST":
        # Pegar o email dessa maneira: request.POST["email"]

        # Verifica se o e-mail já não está no pré-registro e é válido
        # Se alguma das situações acima ocorrer, renderizar novamente a página enviando uma mensagem de erro
        # Se não houverem erros
        # Salvar o registro na tabela pre_register
        # Enviar o e-mail para o usuario (desafio)

        try:
            form = PreRegisterForm(request.POST)

            if form.is_valid():
                email = form.cleaned_data["email"]
                # Verifica se o e-mail já não está cadastrado na tabela de usuários (users)
            
                if email_already_exists_in_users(email):
                    form.add_error("email", "O e-mail informado já está cadastrado no sistema.")

                if email_alreads_exists_in_pre_register(email):
                    form.add_error("email", "O e-mail informado já está em processo de pré-cadastro. Verifique seu e-mail.")

                if not form.is_valid():
                    return render(
                        request,
                        "register/pre_register.html",
                        {"form": form}
                    )
                
        except Exception as exc:
            print(f"Erro ao receber os dados do formulário: {exc}")
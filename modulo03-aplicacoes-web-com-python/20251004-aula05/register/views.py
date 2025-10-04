from django.shortcuts import render

from .forms import PreRegisterForm

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
        # Verifica se o e-mail já não está cadastrado na tabela de usuários (users)
        # Verifica se o e-mail já não está no pré-registro e é válido
        # Se alguma das situações acima ocorrer, renderizar novamente a página enviando uma mensagem de erro
        # Se não houverem erros
        # Salvar o registro na tabela pre_register
        # Enviar o e-mail para o usuario (desafio)
        pass
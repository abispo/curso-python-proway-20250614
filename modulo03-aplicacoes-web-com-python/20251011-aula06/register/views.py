from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import PreRegisterForm
from .models import PreRegister
from .validators import email_already_exists_in_users, email_alreads_exists_in_pre_register
from .utils import send_pre_register_email

def pre_register(request):

    if request.method == "GET":

        form = PreRegisterForm()

        return render(
            request,
            "register/pre_register.html",
            {"form": form}
        )
    
    elif request.method == "POST":
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
                
                pre_register = PreRegister(email=email)
                pre_register.save()

                send_pre_register_email(request=request, pre_register=pre_register)

                return redirect(reverse("register:pre_register_email_sent"))
                
        except Exception as exc:
            print(f"Erro ao receber os dados do formulário: {exc}")


def pre_register_email_sent(request):
    return render(
        request,
        "register/pre_register_email_sent.html"
    )


def register(request):
    return render(
        request,
        "register/register.html"
    )
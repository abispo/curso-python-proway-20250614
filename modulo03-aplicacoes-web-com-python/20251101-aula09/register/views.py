
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.http.request import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone

from core.models import User
from core.validators import all_fields_are_filled

from .exceptions import InvalidPreRegister, ExpiredPreRegister
from .forms import PreRegisterForm
from .models import PreRegister
from .validators import (
    email_already_exists_in_users,
    email_alreads_exists_in_pre_register,
    username_already_exists,
    passwords_match
)
from .utils import send_pre_register_email

def pre_register(request: HttpRequest):

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


def pre_register_email_sent(request: HttpRequest):
    return render(
        request,
        "register/pre_register_email_sent.html"
    )


def register(request: HttpRequest):

    if request.method == "GET":
        try:
            redirect_to = "register:invalid_pre_register"
            token = request.GET["id"]

            # Buscamos por um registro onde o token seja igual ao que recebemos, e o pre registro esteja válido
            pre_register = PreRegister.objects.filter(
                # https://docs.djangoproject.com/en/5.2/ref/models/querysets/#operators-that-return-new-querysets
                Q(token=token) & Q(is_valid=True)
            ).first()

            if not pre_register:
                raise InvalidPreRegister()
            
            expired_pre_register = (timezone.now() - pre_register.created_at).total_seconds() > 86400

            if expired_pre_register:
                pre_register.is_valid = False
                pre_register.save()
                redirect_to = "register:expired_pre_register"
                raise ExpiredPreRegister()

            return render(
                request,
                "register/register.html",
                {"pre_register": pre_register}
            )
        
        except (ValidationError, KeyError):
            return redirect(reverse(redirect_to))
        
    if request.method == "POST":
        try:
            # Recebemos os valores do formulário
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            username = request.POST["username"]
            email = request.POST["email"]
            password = request.POST["password"]
            password_confirm = request.POST["password_confirm"]

            pre_register = PreRegister.objects.filter(email=email).first()

            errors = []

            # Fazemos algumas validações
            if not all_fields_are_filled(first_name, last_name, username, email, password, password_confirm):
                errors.append("Você deve preencher todos os campos do formulário.")

            if username_already_exists(username=username):
                errors.append("Esse nome de usuário já existe.")

            if not passwords_match(password=password, password_confirm=password_confirm):
                errors.append("Os valores das senhas são diferentes.")

            # Caso alguma validação tenha falhado, mostramos a mensagem na tela

            if errors:
                return render(
                    request,
                    "register/register.html",
                    {
                        "pre_register": pre_register,
                        "errors": errors
                    }
                )
            
            # Criamos o registro na tabela users
            user = User.objects.create_user(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=password
            )

            # Para todo usuário que se cadastrar pelo formulário, automaticamente estará associado ao grupo "Clientes"
            # Poderíamos também ter usado a abordagem de django signals
            clients_group, _ = Group.objects.get_or_create(
                name="Clientes"
            )

            user.groups.add(clients_group)
            user.save()

            # Definimos o pré-registro do usuário como inválido (pois finalizou o cadastro)
            pre_register.is_valid = False
            pre_register.save()

            return redirect(reverse("register:register_done"))

        except:
            pass


def invalid_pre_register(request: HttpRequest):

    return render(
        request,
        "register/invalid_pre_register.html"
    )


def expired_pre_register(request: HttpRequest):
    return render(
        request,
        "register/expired_pre_register.html"
    )


def register_done(request: HttpRequest):
    return render(
        request,
        "register/register_done.html"
    )
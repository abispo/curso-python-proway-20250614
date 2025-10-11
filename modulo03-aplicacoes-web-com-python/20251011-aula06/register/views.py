
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone

from .exceptions import InvalidPreRegister, ExpiredPreRegister
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

    return render(
        request,
        "register/register.html"
    )

def invalid_pre_register(request):
    return render(
        request,
        "register/invalid_pre_register.html"
    )

def expired_pre_register(request):
    return render(
        request,
        "register/expired_pre_register.html"
    )
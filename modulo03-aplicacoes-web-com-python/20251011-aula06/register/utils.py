from django.core.mail import send_mail
from django.http.request import HttpRequest
from django.urls import reverse

from .models import PreRegister

def send_pre_register_email(request: HttpRequest, pre_register: PreRegister):
    message = """
Você ou alguém fez um pré-registro no sistema de helpdesk.
Caso queira se cadastrar, clique no link abaixo.
Caso não tenha sido você que fez o pré-registro, apenas ignore esse e-mail

{}{}{}?id={}
""".format(
    "https://" if request.is_secure() else "http://",
    request.get_host(),
    "127.0.0.1",
    pre_register.token
)
    
    send_mail(
        subject="Pré-registro no sistema de helpdesk",
        message=message,
        from_email="admin@localhost",
        recipient_list=[pre_register.email]
    )
from core.models import User

from .models import PreRegister

def email_already_exists_in_users(email: str) -> bool:
    return User.objects.filter(email=email).exists()

def email_alreads_exists_in_pre_register(email: str) -> bool:
    return PreRegister.objects.filter(
        email=email, is_valid=True
    ).exists()

def username_already_exists(username: str) -> bool:
    return User.objects.filter(username=username).exists()

def passwords_match(password: str, password_confirm: str) -> bool:
    return password == password_confirm

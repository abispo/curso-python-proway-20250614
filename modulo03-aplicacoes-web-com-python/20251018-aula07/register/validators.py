from core.models import User

from .models import PreRegister

def email_already_exists_in_users(email: str) -> bool:
    return User.objects.filter(email=email).exists()

def email_alreads_exists_in_pre_register(email: str) -> bool:
    return PreRegister.objects.filter(
        email=email, is_valid=True
    ).exists()

def all_fields_are_filled(*args) -> bool:
    return all(args)
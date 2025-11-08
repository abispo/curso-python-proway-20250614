from django.core.exceptions import ValidationError


class InvalidPreRegister(ValidationError):
    def __init__(self, message = "Pré-registro inválido"):
        super().__init__(message=message)


class ExpiredPreRegister(ValidationError):
    def __init__(self, message = "Pré-registro expirado"):
        super().__init__(message)
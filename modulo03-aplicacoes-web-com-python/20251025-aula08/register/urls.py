from django.urls import path

from . import views

app_name = "register"

urlpatterns = [
    path("", views.register, name="register"),
    path("pre-register/", views.pre_register, name="pre_register"),
    path("pre-register-email-sent/", views.pre_register_email_sent, name="pre_register_email_sent"),
    path("pre-register/invalid/", views.invalid_pre_register, name="invalid_pre_register"),
    path("pre-register/expired/", views.expired_pre_register, name="expired_pre_register"),
    path("done/", views.register_done, name="register_done"),
]

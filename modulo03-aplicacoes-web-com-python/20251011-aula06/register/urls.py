from django.urls import path

from . import views

app_name = "register"

urlpatterns = [
    path("pre-register/", views.pre_register, name="pre_register"),
    path("pre-register-email-sent/", views.pre_register_email_sent, name="pre_register_email_sent"),
    path("", views.register, name="register")
]
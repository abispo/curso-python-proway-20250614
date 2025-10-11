from django.urls import path

from . import views

app_name = "register"

urlpatterns = [
    path("pre-register/", views.pre_register, name="pre_register"),
]
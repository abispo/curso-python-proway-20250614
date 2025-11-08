from django.contrib.auth.decorators import login_required
from django.http.request import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse

from core.models import User
from core.validators import all_fields_are_filled

from .validators import parse_date

def me(request: HttpRequest):
    return render(request, "users/me.html")


@login_required
def profile(request: HttpRequest):
    
    if request.method == "GET":
        return render(
            request,
            "users/profile.html"
        )
    
    elif request.method == "POST":

        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        birth_date = request.POST["birth_date"]

        errors = []

        if not all_fields_are_filled(first_name, last_name):
            errors.append("Nome e sobrenome são obrigatórios!")

        if errors:
            return render(
                request,
                "users/profile.html",
                {"errors": errors}
            )
        
        user: User = request.user
        user.first_name = first_name
        user.last_name = last_name
        user.birth_date = parse_date(birth_date)

        user.save()

        return redirect(reverse("users:me"))
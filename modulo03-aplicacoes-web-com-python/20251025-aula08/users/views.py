from django.http.request import HttpRequest
from django.shortcuts import render

def me(request: HttpRequest):
    return render(request, "users/me.html")

def profile(request: HttpRequest):
    return render(
        request,
        "users/profile.html"
    )
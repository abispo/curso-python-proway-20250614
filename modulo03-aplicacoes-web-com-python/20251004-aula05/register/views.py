from django.shortcuts import render

from .forms import PreRegisterForm

def pre_register(request):

    if request.method == "GET":

        form = PreRegisterForm()

        return render(
            request,
            "register/pre_register.html",
            {"form": form}
        )
    
    elif request.method == "POST":
        pass
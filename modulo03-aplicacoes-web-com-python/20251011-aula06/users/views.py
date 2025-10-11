from django.shortcuts import render

def me(request):
    return render(request, "users/me.html")
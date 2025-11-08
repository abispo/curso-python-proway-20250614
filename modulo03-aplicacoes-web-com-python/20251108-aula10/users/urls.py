from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("me/", views.me, name="me"),
    path("me/profile", views.profile, name="profile")
]
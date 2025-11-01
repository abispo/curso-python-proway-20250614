from django.urls import path

from . import views

app_name = "tickets"

urlpatterns = [
    path("", views.TicketListView.as_view(), name="list_tickets"),
    path("new/", views.TicketCreateView.as_view(), name="create_ticket"),
]

from django.conf import settings
from django.db import models

class Ticket(models.Model):

    STATUS_CHOICES = [
        ("open", "Aberto",),
        ("in_progress", "Em andamento",),
        ("closed", "Fechado",),
        ("cancelled", "Cancelado",),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    description_resolved = models.TextField()
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="open")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "tickets"

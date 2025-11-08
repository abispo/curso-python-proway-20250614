from uuid import uuid4

from django.db import models

class PreRegister(models.Model):
    email = models.CharField("E-mail", max_length=100)
    token = models.UUIDField(default=uuid4, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_valid = models.BooleanField(default=True)

    class Meta:
        db_table = "pre_register"
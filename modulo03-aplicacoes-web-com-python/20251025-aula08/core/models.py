from django.contrib.auth.models import AbstractUser
from django.db.models import DateField

class User(AbstractUser):

    birth_date = DateField("Data de Nascimento", editable=True, blank=True, null=True)
    
    class Meta:
        db_table = "users"
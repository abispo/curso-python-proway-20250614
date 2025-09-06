from django.db import models
from django.utils import timezone

class Pergunta(models.Model):
    texto_pergunta = models.CharField(max_length=100)
    data_publicacao = models.DateTimeField("Data de publicação")

    class Meta:
        db_table = "perguntas"

    def __str__(self):
        return self.texto_pergunta
    
    def publicado_recentemente(self):
        return self.data_publicacao >= timezone.now() - timezone.timedelta(days=1)

class Opcao(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    texto_opcao = models.CharField(max_length=100)
    votos = models.IntegerField(default=0)

    class Meta:
        db_table = "opcoes"
        verbose_name_plural = "Opções"

    def __str__(self):
        return f"{self.texto_opcao} ({self.pergunta.texto_pergunta})"
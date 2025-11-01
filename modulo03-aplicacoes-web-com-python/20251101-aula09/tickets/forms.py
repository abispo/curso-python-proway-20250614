from django import forms

from .models import Ticket


class TicketCreateForm(forms.ModelForm):

    class Meta:

        # A model que será referenciada
        model = Ticket

        # O atributo fields define quais os campos da model serão mostrados no formulário. Caso não indiquemos o atributo widgets, o django automaticamente gere no html os elementos correspondentes aos tipos de dados na model
        fields = ["title", "description"]

        # O atributo widgets é um dicionário onde podemos definir com mais controle como serão os elementos HTML que serão gerados a partir dos campos da model. No caso abaixo, além de definir os tipos de elementos, também podemos definir outras coisas, como as classes CSS que serão atribuídas aos elementos.
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Título do Ticket",
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Descreva o problema.",
                "style": "height: 150px"
            })
        }

        # Também podemos definir métodos para fazer validações customizadas em cada elemento que será mostrado no formulário. Abaixo definimos uma validação para o campo title, que gera uma exceçao caso o valor desse campo tenha menos de 5 caracteres.
        # Para criar esses métodos de validação, basicamente colocamos o sufixo 'clean_' na frente do nome do campo
        def clean_title(self):
            title = self.cleaned_data.get("title")

            if len(title) < 5:
                raise forms.ValidationError("O título do ticket deve ter 5 ou mais caracteres.")
            return title

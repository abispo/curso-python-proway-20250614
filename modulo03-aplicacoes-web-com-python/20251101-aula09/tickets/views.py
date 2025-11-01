from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import TicketCreateForm
from .models import Ticket

class TicketListView(ListView):
    # A model a que esse CBV (Class Based View) está atrelado. O Django utiliza o nome da model para definir algumas coisas, como objeto de contexto, nome de template, etc..
    model = Ticket

    # Por padrão, caso não definirmos o context_object_name, será passado para o template como o nome da model concatenado com o texto _list. Nesse caso, o padrão seria ticket_list
    context_object_name = "tickets"

    # Por padrão, caso não definirmos o template_name, a CBV tentará carregar o seguinte caminho para o template: nome da model pluralizado + nome da model seguido de _list.html.
    # Nesse caso, por padrão o caminho do template a ser renderizado será 'tickets/ticket_list.html'
    template_name = "detalhe_ticket.html"

    # O método get_template_names define a lista de templates que serão procurados antes do django gerar o erro TemplateDoesNotExist. Caso não implementemos esse método, ele vai retornar o nome padrão do template que o django define (tickets/ticket_detail.html)
    def get_template_names(self) -> list[str]:
        return ['detalhe_ticket.html', 'tickets/ticket_list.html']
    
    # O método get_context_data permite redefinirmos as variáveis de contexto que serão injetadas no template. No caso abaixo, além das variáveis padrão, estamos injetando outra variável, chamada mensagem, pois estamos chamando o método get_context_data da classe mãe (ListView)
    def get_context_data(self):
        return super().get_context_data(mensagem="Outro teste")
    

class TicketCreateView(CreateView):
    # É a model da qual vamos adicionar um registro
    model = Ticket

    # Aqui definimos o formulário que será renderizado no template. O Django irá injetar a variável de contexto referente a esse form no template
    form_class = TicketCreateForm

    # Caso não definirmos o nome do template, o padrão seria 'tickets/ticket_form.html'
    template_name = "tickets/ticket_create_form.html"

    # Aqui indicamos pra qual endereço do site o usuário será redirecionado caso o cadastro tenha sido feito com sucesso.
    success_url = reverse_lazy("tickets:list_tickets")
    
    # Esse método é chamado sempre que os dados do formulário são validados com sucesso. Nesse caso, após esses dados terem sido validados, preenchemos os campos owner e status com o usuário que abriu o ticket e o status inicial do ticket, respectivamente
    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.status = "open"
        return super().form_valid(form)
    
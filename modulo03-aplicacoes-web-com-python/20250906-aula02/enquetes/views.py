from django.http import HttpResponse

def index(request):
    return HttpResponse("Olá! Você está na página principal das enquetes.")

def detalhes(request, pergunta_id):
    return HttpResponse(f"Você está na página de detalhes da pergunta '{pergunta_id}'.")

def resultados(request, pergunta_id):
    return HttpResponse(f"Você está na página de resultados da pergunta '{pergunta_id}'.")

def votar(request, pergunta_id):
    return HttpResponse(f"Você está votando em uma opção da pergunta '{pergunta_id}'.")
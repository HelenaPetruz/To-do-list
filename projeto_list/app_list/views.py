from django.shortcuts import render
from .models import Tarefa

def home(request):
    return render(request,'home.html')

def tarefas(request):
    #salva os usuarios da tela para o banco de dados
    nova_tarefa = Tarefa()
    nova_tarefa.titulo = request.POST.get('titulo')
    nova_tarefa.descricao = request.POST.get('descricao')
    nova_tarefa.save()
    #exibí-los numa nova página:
    tarefas = {
        'tarefas': Tarefa.objects.all()
    }
    #retornar para página de listagem
    return render(request, 'tarefas.html', tarefas)
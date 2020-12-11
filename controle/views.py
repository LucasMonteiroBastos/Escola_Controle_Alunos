from django.shortcuts import render

def home(request):
    nome = 'Alunos'
    return render(request, 'controle.html', {'nome': nome})
from django.shortcuts import render
from .models import Aluno

def home(request):
    aluno = Aluno.objects.all()
    return render(request, 'controle.html', {'aluno': aluno})
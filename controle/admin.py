from django.contrib import admin
from .models import Aluno,Matricula, Turno,Turma

admin.site.register(Aluno)
admin.site.register(Matricula)
admin.site.register(Turno)
admin.site.register(Turma)

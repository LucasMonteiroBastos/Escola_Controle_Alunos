from django.db import models

class Matricula(models.Model):
    matricula = models.CharField(max_length=11)

    def __str__(self):
        return self.matricula

class Turma(models.Model):
    turma = models.CharField(max_length=3)

    def __str__(self):
        return self.turma


class Turno(models.Model):
    turno = models.CharField(max_length=20)

    def __str__(self):
        return self.turno




class Aluno(models.Model):
    matricla = models.ForeignKey(Matricula, on_delete=models.PROTECT)
    turma = models.ForeignKey(Turma,on_delete=models.PROTECT)
    turno = models.ForeignKey(Turno, max_length=20, on_delete=models.PROTECT)
    nome = models.CharField(max_length=100)
    disciplina = models.CharField(max_length=20)


    def __str__(self):
        return self.nome



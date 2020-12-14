from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response

from .models import Aluno
from rest_framework import generics
from .serializes import AlunoSerializer


def home(request):
    aluno = Aluno.objects.all()
    return render(request, 'controle.html', {'aluno': aluno})


class ApiHome(generics.ListCreateAPIView):
    model = Aluno
    queryset = model.objects.all()
    serializer_class = AlunoSerializer


class ApiHomeJson(generics.ListAPIView):
    model = Aluno
    queryset = model.objects.all()
    serializer_class = AlunoSerializer


class Json(generics.ListAPIView):
    model = Aluno
    queryset = model.objects.all()
    serializer_class = AlunoSerializer

    def get(self, request, *args, **kwargs):
        alunos = self.get_queryset()
        serializer = self.serializer_class(alunos, many=True)
        return Response(serializer.data)

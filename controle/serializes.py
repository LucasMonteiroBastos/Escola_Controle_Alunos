from rest_framework import serializers

from controle.models import Aluno, Matricula


# Class Aluno => Serializando.
class MatriculaSerializer(serializers.Serializer):
    class Meta:
        model = Matricula
        fields = '__all__'


# Class Aluno => Serializando.
class AlunoSerializer(serializers.Serializer):
    matricla = MatriculaSerializer(many=False)
    class Meta:
        model = Aluno
        fields = '__all__'

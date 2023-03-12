from rest_framework import serializers
from .models import *

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'
        
class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'
    
class FrequenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frequencia
        fields = '__all__'

class PlanoAulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanoAula
        fields = '__all__'

class AtividadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atividade
        fields = '__all__'

class AtividadeAlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtividadeAluno
        fields = '__all__'

class DisciplinaAlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisciplinaAluno
        fields = '__all__'


class FrequenciaAlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrequenciaAluno
        fields = '__all__'
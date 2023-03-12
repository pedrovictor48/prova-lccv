from rest_framework import viewsets
from .models import *
from .serializers import *

class AlunosViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

class FrequenciaViewSet(viewsets.ModelViewSet):
    queryset = Frequencia.objects.all()
    serializer_class = FrequenciaSerializer

class PlanoAulaViewSet(viewsets.ModelViewSet):
    queryset = PlanoAula.objects.all()
    serializer_class = PlanoAulaSerializer

class FrequenciaViewSet(viewsets.ModelViewSet):
    queryset = PlanoAula.objects.all()
    serializer_class = FrequenciaSerializer


class AtividadeViewSet(viewsets.ModelViewSet):
    queryset = PlanoAula.objects.all()
    serializer_class = AtividadeSerializer

class AtividadeAlunoViewSet(viewsets.ModelViewSet):
    queryset = PlanoAula.objects.all()
    serializer_class = AtividadeAlunoSerializer

class DisciplinaAlunoViewSet(viewsets.ModelViewSet):
    queryset = PlanoAula.objects.all()
    serializer_class = DisciplinaAlunoSerializer

class FrequenciaAlunoViewSet(viewsets.ModelViewSet):
    queryset = PlanoAula.objects.all()
    serializer_class = FrequenciaAlunoSerializer

## swagger

from django.contrib import admin

# Register your models here.
from .models import Aluno, Professor, Atividade, Disciplina, AtividadeAluno, DisciplinaAluno, FrequenciaAluno


admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Atividade)
admin.site.register(Disciplina)
admin.site.register(AtividadeAluno)
admin.site.register(DisciplinaAluno)
admin.site.register(FrequenciaAluno)
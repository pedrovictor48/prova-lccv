from django.contrib import admin
from django import forms

# Register your models here.
from .models import Aluno, Professor, Atividade, Disciplina, AtividadeAluno, DisciplinaAluno, FrequenciaAluno, PlanoAula, Frequencia

# inlines
class DisciplinaAlunoInline(admin.TabularInline):
    model = DisciplinaAluno
    extra = 2
    readonly_fields = ['nota']


class AtividadeAlunoInline(admin.TabularInline):
    model = AtividadeAluno
    extra = 1

class FrequenciaAlunoInline(admin.TabularInline):
    model = FrequenciaAluno
    extra = 1

#forms
@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    inlines = [DisciplinaAlunoInline, AtividadeAlunoInline]

@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    pass

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    pass

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    pass

@admin.register(PlanoAula)
class PlanoAulaAdmin(admin.ModelAdmin):
    pass

@admin.register(Frequencia)
class FrequenciaAdmin(admin.ModelAdmin):
    inlines = [FrequenciaAlunoInline]

# signals para lidar com o negocio do somatorio
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

@receiver(post_delete, sender=AtividadeAluno)
def decrementarNota(sender, instance, using, **kwargs):
    t = DisciplinaAluno.objects.filter(id_disciplina=instance.id_atividade.id_disciplina).filter(id_aluno=instance.id_aluno.id_aluno).get()
    #quando removo eu decremento da nota
    t.nota -= instance.nota
    t.save()


@receiver(post_save, sender=AtividadeAluno)
def decrementarNota(sender, instance, using, **kwargs):
    t = DisciplinaAluno.objects.filter(id_disciplina=instance.id_atividade.id_disciplina).filter(id_aluno=instance.id_aluno.id_aluno).get()
    #quando adiciono eu incremento
    t.nota += instance.nota
    t.save()
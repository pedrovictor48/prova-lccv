#vou usar signals para realizar aquele processo da soma
from .models import *
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

@receiver(post_delete, sender=AtividadeAluno)
def decrementarNota(sender, instance, using, **kwargs):
    t = DisciplinaAluno.objects.filter(id_disciplina=instance.id_atividade.id_disciplina).filter(id_aluno=instance.id_aluno.id_aluno)
    print(t.value)


@receiver(post_save, sender=AtividadeAluno)
def decrementarNota(sender, instance, using, **kwargs):
    t = DisciplinaAluno.objects.filter(id_disciplina=instance.id_atividade.id_disciplina).filter(id_aluno=instance.id_aluno.id_aluno)
    print(t.value)
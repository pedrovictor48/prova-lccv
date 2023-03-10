from django.db import models

class Professor(models.Model):
    id_professor = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=8)
    codigo = models.CharField(max_length=8)
    telefone = models.CharField(max_length=11)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    id_disciplina = models.BigAutoField(primary_key=True)
    id_professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    codigo = models.CharField(max_length=7)
    carga_horaria = models.IntegerField()
    ementa = models.TextField(blank=True) # ver a questao do clob!

    def __str__(self):
        return f"{self.codigo} - {self.nome}"

class Aluno(models.Model):
    id_aluno = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=8)
    matricula = models.CharField(max_length=8)
    telefone = models.CharField(max_length=11)
    email = models.EmailField()
    disciplinas = models.ManyToManyField(Disciplina)

    def __str__(self):
        return self.nome


class PlanoAula(models.Model):
    id_plano_aula = models.BigAutoField(primary_key=True)
    id_disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    tema_aula = models.CharField(max_length=255)
    conteudo = models.TextField()
    metodo = models.CharField(max_length=50)
    dia = models.DateField()

class Atividade(models.Model):
    TIPOS_ATIVIDADES = [
        ('atividade_casa', 'Atividade de casa'),
        ('atividade_sala', 'Atividade de sala'),
        ('prova', 'Prova') 
    ]
    
    id_atividade = models.BigAutoField(primary_key=True)
    atividade = models.TextField()
    tipo = models.CharField(max_length=50, choices=TIPOS_ATIVIDADES)  
    data_postagem = models.DateField()
    data_entrega = models.DateField(blank=True)
    id_disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    id_plano_aula = models.ForeignKey(PlanoAula, on_delete=models.CASCADE)

class Frequencia(models.Model):
    id_frequencia = models.BigAutoField(primary_key=True)
    id_materia = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    dia = models.DateField()

# Tabelas que representam relacionamentos

class AtividadeAluno(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)
    id_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    nota = models.FloatField(blank=True)

class FrequenciaAluno(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    id_frequencia = models.ForeignKey(Frequencia, on_delete=models.CASCADE)
    presenca = models.BooleanField(default=True) # ver a questao do booelan ou char(1)
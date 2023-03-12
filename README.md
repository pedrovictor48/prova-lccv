# prova-lccv

## Algumas considerações

1. Usei signals para implementar o field da soma em DisciplinaAluno, toda vez que uma instancia de AtividadeAluno é adicionada ou deletada, a instancia correspondente de DisciplinaAluno tem o field nota alterado
2. No campo presenca em AlunoFrequencia, coloquei do tipo BooleanField com valor padrão sendo True, pois deixa a interface mais intuitiva
3. Usei TabularInlines para deixar a interface no DjangoAdmin mais intuitiva, por ex: ao invés de precisar adicionar uma instância de AtividadeAluno, como se fosse uma tabela separada, o Administrador pode adicionar a partir de uma instância de Aluno, o que faz mais sentido do ponto de vista de Usuário

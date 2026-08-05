from rich import print, inspect
from aluno import Aluno
from professor import Professor
from funcionario import Funcionario


a1 = Aluno("Jony", 29, "ADS", "EAD")
a1.fazer_aniversario()
a1.fazer_matricula()
# inspect(a1, methods=True)

p1 = Professor("Samuel", 35, "Informática", "mestre")
p1.fazer_aniversario()
p1.dar_aula()
# inspect(p1, methods=True)

f1 = Funcionario("Claudia", 26, "Secretária", "Secretaria")
f1.fazer_aniversario()
f1.bater_ponto()
# inspect(f1, methods=True)
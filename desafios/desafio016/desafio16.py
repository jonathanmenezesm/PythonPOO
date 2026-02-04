# Crie uma classe Funcionario, onde podemos cadastrar: nome, setor e cargo. Crie também um método que permita ao funcionário se apresentar.

#Apresentar > "Olá, eu sou {nome} e sou {cargo} do setor de {setor}.

class Funcionario:
    def __init__(self, nome, setor, cargo, empresa="Genérica"):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        self.empresa = empresa

    def apresentar(self):
        if self.empresa == "Genérica":
            print(f"Olá, eu me chamo {self.nome} e sou {self.cargo} do setor {self.setor}.")
        else:
            print(f"Olá, eu me chamo {self.nome} e sou {self.cargo} do setor {self.setor} na empresa {self.empresa}.")


f1 = Funcionario("Bruno Fonseca", setor="CyberSecurity", cargo="Analista Jr")
f1.apresentar()

f2 = Funcionario("Gustavo Lima", setor="Sertanejo", cargo="Cantor", empresa="Spotify")
f2.apresentar()
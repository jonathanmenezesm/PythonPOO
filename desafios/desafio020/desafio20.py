# 🎮 Crie a classe Gamer, onde podemos cadastrar nome, nick e os jogos favoritos de uma pessoa.
# 🎮 Crie também um método que permita mostrar a ficha desse gamer.
from openpyxl.styles.builtins import title
# j1 = Gamer(nome="Fabricio da Silva", nick="detonator2025")
# j1.add_favoritos("Mario Bros.")
# j1.add_favoritos("Sonic")
# j1.add_favoritos("God of War")
# j1.add_favoritos("Fortnite")
# j1.ficha()
#
# Jogador <detonator2025>
# Nome real: Fabricio da Silva
# Jogos favoritos:
#   Fortnite
#   God of War
#   Mario Bros.
#   Sonic

from rich import print
from rich.panel import Panel




class Gamer():
    def __init__(self, nome, nick, jogos_favoritos=""):
        self.nome = nome
        self.nick = nick
        self.jogos_favoritos = []

    def add_favoritos(self, jogo):
        self.jogos_favoritos.append(jogo)


    def ficha(self):
        texto = f" Nome real: [black on blue] {self.nome} [/]\n"
        texto += "Jogos favoritos:\n"
        for jogo in sorted(self.jogos_favoritos):
            texto += f"🎮 [blue]{jogo}[/]\n"   # ícone + cor

        caixa = Panel(texto, title=f"Jogador <{self.nick}>", width=50)
        print(caixa)


j1 = Gamer("Jonathan Moura", "JotaM")
j1.add_favoritos("Mario")
j1.add_favoritos("God of War")
j1.add_favoritos("Zelda")
j1.ficha()



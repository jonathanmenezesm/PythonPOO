# 📺 Crie a classe ControleRemoto, onde vamos simular o funcionamento
# 📺 de um controle simples (canal, volume e liga/desliga)

# < Diminui o canal
# > aumenta o canal
# + Aumenta volume
# - Diminui o volume
# @ liga/desliga a tv
# 0 sai do programa
from rich import print
from rich.panel import Panel
import os

def clear():
    os.system("cls")

class ControleRemoto:
    def __init__(self, volume=1, canal=1, estado=False):
        self.volume = volume
        self.canal = canal
        self.estado = estado

    def ligar(self):
        if self.estado == False:
            self.estado = True
        else:
            pass

    def desligar(self):
        if self.estado == True:
            self.estado = False
        else:
            pass

    def aumentar(self, valor=1):
        if self.volume + valor <= 10:  # limite máximo
            self.volume += valor
        else:
            self.volume = 10

    def diminuir(self, valor=1):
        if self.volume - valor >= 0:
            self.volume -= valor
        else:
            self.volume = 0

    def passarCanal(self, passar=1):
        if self.canal + passar > 13:
            self.canal = 1
        else:
            self.canal += passar

    def voltarCanal(self, voltar=1):
        if self.canal - voltar < 1:
            self.canal = 13
        else:
            self.canal -= voltar


t1 = ControleRemoto()

while True:
    CH = t1.canal
    VOL = t1.volume

    if t1.estado == False:
        clear()
        caixa = Panel("[red]A TV está desligada! [/]", title="[ TV ]", width=35)
        print(caixa)
    else:
        clear()

        #volume
        bloco = "█" * t1.volume  # blocos preenchidos
        vazio = "█" * (10 - t1.volume)  # blocos vazios
        barra_volume = f"[green]{bloco}[/][grey]{vazio}[/]"

        #canais
        canais = ""
        for i in range(1, 14):
            if i == t1.canal:
                canais += f"[black on yellow] {i} [/] "
            else:
                canais += f"{i} "

        caixa = Panel(f"Canal: {canais}\nVolume: {barra_volume}", title="[ TV ]", width=45)
        print(caixa)

    comando = input(f'<CH {CH}>  <VOL {VOL}> ')

    if comando == "<":
        t1.voltarCanal()
    elif comando == ">":
        t1.passarCanal()
    elif comando == "+":
        t1.aumentar()
    elif comando == "-":
        t1.diminuir()
    elif comando == "@":
        if t1.estado:
            t1.desligar()
        else:
            t1.ligar()
    elif comando == "0":
        print("Saindo do programa...")
        break
    else:
        print("Comando inválido!")




# 📺 Crie a classe ControleRemoto, onde vamos simular o funcionamento
# 📺 de um controle simples (canal, volume e liga/desliga)

# < Diminui o canal
# > aumenta o canal
# + Aumenta volume
# - Diminui o volume
# @ liga/desliga a tv
# 0 sai do programa

class ControleRemoto:
    def __init__(self, volume, canal, estado=False):
        self.volume = volume
        self.canal = canal
        self.estado = estado


    def ligar(self):
        if self.estado == False:
            self.estado = True
            print("LIGANDO A TV...")
            print("TV LIGADA!")
        else:
            print("A TV JÁ ESTÁ LIGADA!")


    def desligar(self):
        if self.estado == True:
            self.estado = False
            print("DESLIGANDO A TV...")
            print("TV DESLIGADA!")
        else:
            print("A TV JÁ ESTÁ DESLIGADA!")

    def aumentar(self, valor=1):
        if self.volume + valor <= 10:  # limite máximo
            self.volume += valor
        else:
            self.volume = 10
        print(f"Volume: {self.volume}")

    def diminuir(self, valor=1):
        if self.volume - valor >= 0:
            self.volume -= valor
        else:
            self.volume = 0
        print(f'Volume: {self.volume}')

    def passarCanal(self, passar=1):
        if self.canal + passar > 13:
            self.canal = 1
        else:
            self.canal += passar
        print(f'Canal: {self.canal}')


    def voltarCanal(self, voltar=1):
        if self.canal - voltar < 1:
            self.canal = 13
        else:
            self.canal -= voltar
        print(f'Canal: {self.canal}')


t1 = ControleRemoto(0,1)
t1.ligar()
t1.desligar()
t1.aumentar(5)
t1.diminuir(6)
t1.passarCanal(7)
t1.voltarCanal(8)

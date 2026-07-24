# 🖊️ Crie a classe Caneta, que simule o funcionamento de uma caneta colorida,
# 🖊️ podendo escrever frases na cor relativa.
# OBS.: Crie o metodo destampar(), caso esteja tampada a caneta não escreve e tambem o metodo tampar()

from rich import print

class Caneta:
    def __init__(self, cor, estado=False):
        self.cor = cor
        self.estado = estado
        self.ajustar_cor()


    def ajustar_cor(self):
        if self.cor in ['vermelho','vermelha']:
            self.cor = 'red'
        elif self.cor in ['azul']:
            self.cor = 'blue'
        elif self.cor in ['verde']:
            self.cor = 'green'
        else:
            self.cor = 'white'

    def destampar(self):
        if self.estado == True:
            print(f" :prohibited: A [{self.cor}] caneta [/] já está destampada! :writing_hand:")
        else:
            self.estado = True
            print(f"A [{self.cor}]caneta[/] foi destampada! :pen:")



    def tampar(self):
        if self.estado == False:
            print(f" :prohibited: A [{self.cor}]caneta[/] já está tampada!")
        else:
            self.estado = False
            print(f"A [{self.cor}]caneta[/] foi tampada! :pen:")

    def escrever(self, texto):
        if self.estado == True:
            print(f'[{self.cor}]{texto}[/]')
        else:
            print(f" :prohibited: A [{self.cor}]caneta[/] está tampada!")

    def quebrar_linha(self, n):
        for _ in range(n):
            print()

c1 = Caneta('azul')
c1.destampar()
c1.escrever('Olá, Mundo!')
c1.quebrar_linha(1)
c1.tampar()
c1.escrever('Olá, Mundo!!!')

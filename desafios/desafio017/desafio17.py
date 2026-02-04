#Crie a classe Produto, onde podemos cadastrar: nome e o preço. Crie também um método que mostre uma etiqueta de preço do produto.

# Saida:
# etiqueta() > Um quadrado com etiqueta (usar lib rich) exibindo nome e preço.

from rich.panel import Panel
from rich.console import Console
from rich.align import Align

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        console = Console()
        # conteudo = Align.center(f'{self.nome} \n'
        #                  f'R$ {self.preco:.2f}')
        # etiqueta = Panel(conteudo, title='Etiqueta', width=30)
        etiqueta = Panel(f'{self.nome:^30}\n{"":-^30}\n {self.preco:.^30,.2f}',title="Produto",width=35)
        console.print(etiqueta)

p1 = Produto('Maquina', 500)
p1.etiqueta()

p2 = Produto('Camiseta', 100)
p2.etiqueta()
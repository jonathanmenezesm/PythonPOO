#Crie a classe Produto, onde podemos cadastrar: nome e o preço. Crie também um método que mostre uma etiqueta de preço do produto.

# Saida:
# etiqueta() > Um quadrado com etiqueta (usar lib rich) exibindo nome e preço.

from rich.console import Console

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        console = Console('Teste')
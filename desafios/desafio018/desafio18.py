# Crie uma classe Churrasco(titulo:, quantidade:), onde seja possível informar quantas pessoas vão participar e mostre quanto de carne deve ser comprado, o custo total do churrasco e o preço por pessoa.

# saída:
# considere 400g por pessoa
# preço da carne: R$82,40/kg
# analisar():


# quadrado usando rich
# Analisando "titulo" com "convidados"
# cada participante comerá 0.4kg e cada Kg custa R$82.40
# Recomendo comprar "quantidade_carne" kg de carne
# O custo total será de "custo"
# Cada pessoa pagará "custo individual" para participar do churrasco

from rich.panel import Panel
from rich.console import Console

class Churrasco:
    def __init__(self, titulo, quantidade):
        self.titulo = titulo
        self.quantidade = quantidade
     
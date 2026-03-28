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
        
        
    def analisar(self):
        carne_por_pessoa = 0.4
        preco_carne = 82.40
        
        quantidade_carne = self.quantidade * carne_por_pessoa
        custo_total = quantidade_carne * preco_carne
        custo_individual = custo_total / self.quantidade
        
        console = Console()
        painel = Panel(f"Analisando '{self.titulo}' com {self.quantidade} convidados\n"
                       f"Cada participante comerá {carne_por_pessoa} kg e cada Kg custa R$ {preco_carne:.2f}\n"
                       f"Recomendo comprar {quantidade_carne:.2f} kg de carne\n"
                       f"O custo total será de R$ {custo_total:.2f}\n"
                       f"Cada pessoa pagará R$ {custo_individual:.2f} para participar do churrasco", title="Análise do Churrasco", width=70)
        console.print(painel)
churrasco = Churrasco("Churrasco dos amigos", 10)
churrasco.analisar()
     
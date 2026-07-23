# Crie uma classe Churrasco(titulo:, quantidade:), onde seja possível informar quantas pessoas vão participar
# mostre quanto de carne deve ser comprado,
# o custo total do churrasco e o preço por pessoa.
# saída:
# considere 400g por pessoa
# preço da carne: R$82,40/kg
# analisar():
# quadrado usando rich
# Analisando "titulo" com "convidados"
# cada participante comerá 0.4kg e cada Kg custa R$82.40
#O custo total será de "custo"
# Cada pessoa pagará "custo individual"

from rich.panel import Panel
from rich import print


class Churrasquinho():
    def __init__(self,titulo,quantidadeDePessoas): #construtor
        self.titulo = titulo
        self.quantidadeDePessoas = quantidadeDePessoas

    def analisar(self):
        precoDaCarne = 82.40  # preço da carne/kg
        consumoPadrao = 400 / 1000  # consumo padrão de cada pessoa (dividido por 1000 para converter em gramas)


        quantidadeDeCarneNecessaria = consumoPadrao * self.quantidadeDePessoas
        valorTotalDasCarnes = quantidadeDeCarneNecessaria * precoDaCarne
        valorPorPessoa = (valorTotalDasCarnes / self.quantidadeDePessoas)

        texto = (f"""
        Analisando [green]{self.titulo}[/] evento para [blue]{self.quantidadeDePessoas} pessoas[/]
        Cada pessoa irá consumir 400gr e cada Kg custa R$82,40
        Recomendo [blue]comprar {round(quantidadeDeCarneNecessaria)}kgs[/] de carne
        O custo total será de [green]R${valorTotalDasCarnes:.2f}[/]
        E cada pessoa pagará [yellow]R${valorPorPessoa:.2f}[/] para participar        
        """)

        caixa = Panel(texto, title=self.titulo)

        print(caixa)

c1 = Churrasquinho("Churrascria", 50)
c1.analisar()

from rich import print
from rich.table import Table

tabela = Table(title="Tabela de preços")

tabela.add_column("Nome", justify="left", style="cyan")
tabela.add_column("Preço", justify="center", style="magenta")

tabela.add_row("Lápis", "[green]R$1,50[/]")
tabela.add_row("borracha", "[green]R$2,00[/]")

print(tabela)
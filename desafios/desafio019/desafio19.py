# Crie a classe Livro, que vai simular a passagem de páginas de um livro,
# considerando também se o usuário chegou ao fim da leitura.

#Classe > Titulo e paginas

#terminal
# 📖 Você acabou de abrir o livro '10 coisas que aprendi' que tem 20 páginas no total.
# 📖 Você agora está na página 1
# 📖 ► Pág2 ► Pág3 ► Pág4 ► Pág5 ► Pág6 ► Você avançou 5 páginas e agora está na página 6
# 📖 ► Pág7 ► Pág8 ► Pág9 ► Pág10 ► Pág11 ► Pág12 ► Pág13 ► Pág14 ► Pág15 ► Pág16 ► Você avançou 10 páginas e agora está na página 16

class Livro:
    def __init__(self, titulo, total_paginas):
        self.titulo = titulo
        self.total_paginas = total_paginas
        self.pagina_atual = 1
        print(f"📖 Você acabou de abrir o livro '{self.titulo}' que tem {self.total_paginas} páginas no total. E agora você está na página {self.pagina_atual}")
    
    def avancar_paginas(self, paginas):
        for p in range(self.pagina_atual + 1, self.pagina_atual + paginas + 1):
            print(f"📖 ► Pág{p}", end=" ")
            
        if self.pagina_atual + paginas <= self.total_paginas:
            self.pagina_atual += paginas
            
            print(f"\n📖 Você avançou {paginas} páginas e agora está na página {self.pagina_atual}")
            
# Criando um livro e avançando páginas
livro = Livro("10 coisas que aprendi", 20)
livro.avancar_paginas(5)
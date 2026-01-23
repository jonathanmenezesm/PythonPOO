class Carro:
    def __init__(self, rodas = 4, motor = 1, portas = 4):
        self.rodas = rodas
        self.motor = motor
        self.portas = portas

    #metodos
    def mostrar(self):
        print(f'Rodas: {self.rodas}')
        print(f'Motor: {self.motor}')
        print(f'Portas: {self.portas}')
#instancia
c1 = Carro()
c1.mostrar()

#HERANÇA
class Uno(Carro):
    def __init__(self, rodas = 4, motor = 1, portas = 4, titulo = 'Deus das Estradas'):
        super().__init__(rodas, motor, portas)

        self.titulo = titulo



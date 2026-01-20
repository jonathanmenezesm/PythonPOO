class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depositos
    """
    def __init__(self, id, nome, saldo):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f'Conta {self.id} criada com sucesso. Saldo Atual R${self.saldo:,.2f}')

    def __str__(self):
        return f'A conta {self.id} de {self.titular} tem R${self.saldo:.2f} de saldo'

    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito de R${valor:,.2f} autorizado para conta {self.id}')

    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Saque NEGADO, de R${valor:,.2f} na conta {self.id}: SALDO INSUFICIENTE!")
        else:
            self.saldo -= valor
            print(f'Saque de R${valor:,.2f} autorizado para conta {self.id}')

c1 = ContaBancaria(1542, 'Jonathan', 1000)
c1.depositar(1000)
c1.sacar(1500)
print(c1)
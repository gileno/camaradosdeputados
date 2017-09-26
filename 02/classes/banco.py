import random

class Conta:
    def __init__(self, nome, saldo=0.0):
        self.nome = nome
        self.saldo = saldo
        self.numero = random.randint(1, 1000)
    def imprimir(self):
        print("Nome: %s" % self.nome)
        print("Número: %04d" % self.numero)
        print("Saldo: %.2f" % self.saldo)
    def saque(self, valor):
        if self.saldo < valor:
            raise ValueError("Saldo insuficiente!")
        self.saldo = self.saldo - valor
    def deposito(self, valor):
        self.saldo = self.saldo + valor
    def transferir(self, outra_conta, valor):
        """Recebe uma instância de conta e um valor a ser transferido"""
        self.saque(valor)
        outra_conta.deposito(valor)

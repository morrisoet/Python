from abc import ABC, abstractmethod
from datetime import datetime


class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if self.valor > 0:
            conta._saldo += self.valor
            conta.historico.adicionar_transacao(self)
            print("✅ Depósito realizado com sucesso!")
        else:
            print("❌ Valor inválido para depósito.")


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        excedeu_saldo = self.valor > conta.saldo
        excedeu_limite = self.valor > conta.limite
        excedeu_saques = conta.numero_saques >= conta.limite_saques

        if excedeu_saldo:
            print("❌ Saldo insuficiente.")
        elif excedeu_limite:
            print("❌ Valor do saque excede o limite.")
        elif excedeu_saques:
            print("❌ Número máximo de saques excedido.")
        elif self.valor > 0:
            conta._saldo -= self.valor
            conta.numero_saques += 1
            conta.historico.adicionar_transacao(self)
            print("✅ Saque realizado com sucesso!")
        else:
            print("❌ Valor inválido.")

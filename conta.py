from historico import Historico


class Conta:
    def __init__(self, cliente, numero, agencia="0001"):
        self._saldo = 0.0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    def realizar_transacao(self, transacao):
        transacao.registrar(self)

    def __str__(self):
        return (
            f"Agência: {self.agencia}\n"
            f"Conta: {self.numero}\n"
            f"Titular: {self.cliente.nome}\n"
            f"Saldo: R$ {self.saldo:.2f}"
        )

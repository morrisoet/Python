from conta import Conta


class ContaCorrente(Conta):
    limite = 500
    limite_saques = 3

    def __init__(self, cliente, numero):
        super().__init__(cliente, numero)
        self.numero_saques = 0

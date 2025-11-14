from datetime import datetime


class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        })

    def mostrar(self):
        if not self.transacoes:
            print("Nenhuma movimentação realizada.")
            return

        print("\n===== HISTÓRICO =====")
        for t in self.transacoes:
            print(f"{t['data']} - {t['tipo']}: R$ {t['valor']:.2f}")
        print("=====================")

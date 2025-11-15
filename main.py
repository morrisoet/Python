# =======================
#   SISTEMA BANCÁRIO OOP
# =======================

# ---- Cores ANSI ----
class C:
    HEADER = "\033[95m"
    OK = "\033[92m"
    WARNING = "\033[93m"
    ERROR = "\033[91m"
    BLUE = "\033[94m"
    END = "\033[0m"
    BOLD = "\033[1m"


# ---------------------
#       CLASSES
# ---------------------

class Usuario:
    def __init__(self, nome, cpf, nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento
        self.endereco = endereco

    def __str__(self):
        return f"{self.nome} – CPF: {self.cpf}"


class Conta:
    LIMITE_SAQUE = 500
    MAX_SAQUES = 3

    def __init__(self, agencia, numero, usuario):
        self.agencia = agencia
        self.numero = numero
        self.usuario = usuario
        self.saldo = 0.0
        self.extrato = []
        self.saques_realizados = 0

    # Depósito
    def depositar(self, valor):
        if valor <= 0:
            print(f"{C.ERROR}❌ Valor inválido.{C.END}")
            return

        self.saldo += valor
        self.extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"{C.OK}✔ Depósito realizado com sucesso!{C.END}")

    # Saque
    def sacar(self, valor):
        if valor <= 0:
            print(f"{C.ERROR}❌ Valor inválido.{C.END}")
            return

        if valor > self.saldo:
            print(f"{C.ERROR}❌ Saldo insuficiente.{C.END}")
            return

        if valor > Conta.LIMITE_SAQUE:
            print(f"{C.ERROR}❌ Valor excede o limite de R$ {Conta.LIMITE_SAQUE}.{C.END}")
            return

        if self.saques_realizados >= Conta.MAX_SAQUES:
            print(f"{C.ERROR}❌ Limite de saques excedido.{C.END}")
            return

        self.saldo -= valor
        self.saques_realizados += 1
        self.extrato.append(f"Saque: R$ {valor:.2f}")
        print(f"{C.OK}✔ Saque realizado com sucesso!{C.END}")

    # Extrato
    def mostrar_extrato(self):
        print(f"\n{C.BOLD}{C.BLUE}====== EXTRATO — Conta {self.numero} ======{C.END}")

        if not self.extrato:
            print(f"{C.WARNING}Nenhuma movimentação registrada.{C.END}")
        else:
            for linha in self.extrato:
                print(f"- {linha}")

        print(f"\nSaldo atual: R$ {self.saldo:.2f}")
        print(f"{C.BLUE}=========================================={C.END}")

    def __str__(self):
        return f"Agência: {self.agencia} | Conta: {self.numero} | Titular: {self.usuario.nome}"


# ---------------------------
#  SISTEMA / APLICAÇÃO
# ---------------------------

class SistemaBancario:
    def __init__(self):
        self.usuarios = []
        self.contas = []
        self.AGENCIA = "0001"

    # Criar usuário
    def criar_usuario(self):
        cpf = input("CPF: ")

        if self.buscar_usuario(cpf):
            print(f"{C.WARNING}⚠ Usuário já existe!{C.END}")
            return

        nome = input("Nome completo: ")
        nasc = input("Data de nascimento (dd-mm-aaaa): ")
        end = input("Endereço: ")

        usuario = Usuario(nome, cpf, nasc, end)
        self.usuarios.append(usuario)

        print(f"{C.OK}✔ Usuário criado!{C.END}")

    # Listar usuários
    def listar_usuarios(self):
        if not self.usuarios:
            print(f"{C.WARNING}⚠ Nenhum usuário.{C.END}")
            return

        print(f"\n{C.BOLD}{C.BLUE}===== USUÁRIOS CADASTRADOS ====={C.END}")
        for u in self.usuarios:
            print(f"{u}")
        print(f"{C.BLUE}================================{C.END}")

    # Buscar usuário
    def buscar_usuario(self, cpf):
        for user in self.usuarios:
            if user.cpf == cpf:
                return user
        return None

    # Criar conta
    def criar_conta(self):
        cpf = input("CPF do usuário: ")
        usuario = self.buscar_usuario(cpf)

        if not usuario:
            print(f"{C.ERROR}❌ Usuário não encontrado.{C.END}")
            return

        numero = len(self.contas) + 1
        conta = Conta(self.AGENCIA, numero, usuario)
        self.contas.append(conta)

        print(f"{C.OK}✔ Conta {numero} criada para {usuario.nome}!{C.END}")

    # Listar contas
    def listar_contas(self):
        if not self.contas:
            print(f"{C.WARNING}⚠ Nenhuma conta criada.{C.END}")
            return

        print(f"\n{C.BOLD}{C.BLUE}======= CONTAS ======={C.END}")
        for c in self.contas:
            print(c)
        print(f"{C.BLUE}======================={C.END}")

    # Selecionar conta
    def selecionar_conta(self):
        if not self.contas:
            print(f"{C.WARNING}⚠ Nenhuma conta disponível.{C.END}")
            return None

        self.listar_contas()

        escolha = input("Digite o número da conta ou 'q' para voltar: ")
        if escolha.lower() == "q":
            return None

        try:
            escolha = int(escolha)
        except ValueError:
            print(f"{C.ERROR}❌ Valor inválido.{C.END}")
            return None

        for conta in self.contas:
            if conta.numero == escolha:
                return conta

        print(f"{C.ERROR}❌ Conta não encontrada.{C.END}")
        return None

    # Menu principal
    def menu(self):
        return f"""
{C.BOLD}{C.HEADER}======= SISTEMA BANCÁRIO ======={C.END}
[d] Depositar
[s] Sacar
[e] Extrato
[u] Novo usuário
[lu] Listar usuários
[c] Nova conta
[l] Listar contas
[q] Sair
=================================
"""

    def iniciar(self):
        while True:
            opcao = input(self.menu()).lower()

            if opcao == "u":
                self.criar_usuario()

            elif opcao == "lu":
                self.listar_usuarios()

            elif opcao == "c":
                self.criar_conta()

            elif opcao == "l":
                self.listar_contas()

            elif opcao in ("d", "s", "e"):
                conta = self.selecionar_conta()
                if not conta:
                    continue

                if opcao == "d":
                    valor = float(input("Valor do depósito: "))
                    conta.depositar(valor)

                elif opcao == "s":
                    valor = float(input("Valor do saque: "))
                    conta.sacar(valor)

                elif opcao == "e":
                    conta.mostrar_extrato()

            elif opcao == "q":
                print(f"{C.OK}👋 Saindo... Obrigado por usar o sistema!{C.END}")
                break

            else:
                print(f"{C.ERROR}❌ Opção inválida.{C.END}")


# ------------------------
# EXECUÇÃO DO SISTEMA
# ------------------------
if __name__ == "__main__":
    SistemaBancario().iniciar()

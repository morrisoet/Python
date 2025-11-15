import os
import sys


# ==========================================
#  CORES NO TERMINAL
# ==========================================
class Cores:
    RESET = "\033[0m"
    VERDE = "\033[92m"
    VERMELHO = "\033[91m"
    AMARELO = "\033[93m"
    CIANO = "\033[96m"
    NEGRITO = "\033[1m"


# ==========================================
#  MODELOS ORIENTADOS A OBJETOS
# ==========================================
class Cliente:
    def __init__(self, nome, cpf, nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento
        self.endereco = endereco

    def __repr__(self):
        return f"{self.nome} (CPF: {self.cpf})"


class Conta:
    LIMITE_SAQUES = 3
    LIMITE_VALOR = 500

    def __init__(self, agencia, numero, cliente):
        self.agencia = agencia
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0
        self.extrato = ""
        self.saques_realizados = 0

    # -----------------------------
    #      OPERAÇÕES
    # -----------------------------
    def depositar(self, valor):
        if valor <= 0:
            print(f"{Cores.VERMELHO}❌ Valor inválido.{Cores.RESET}")
            return

        self.saldo += valor
        self.extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"{Cores.VERDE}✅ Depósito realizado com sucesso!{Cores.RESET}")

    def sacar(self, valor):
        if valor <= 0:
            print(f"{Cores.VERMELHO}❌ Valor inválido.{Cores.RESET}")
            return

        if valor > self.saldo:
            print(f"{Cores.VERMELHO}❌ Saldo insuficiente.{Cores.RESET}")
            return

        if valor > Conta.LIMITE_VALOR:
            print(f"{Cores.VERMELHO}❌ O valor excede o limite permitido.{Cores.RESET}")
            return

        if self.saques_realizados >= Conta.LIMITE_SAQUES:
            print(f"{Cores.VERMELHO}❌ Limite diário de saques atingido.{Cores.RESET}")
            return

        self.saldo -= valor
        self.extrato += f"Saque: R$ {valor:.2f}\n"
        self.saques_realizados += 1

        print(f"{Cores.VERDE}✅ Saque realizado com sucesso!{Cores.RESET}")

    def mostrar_extrato(self):
        print("\n========== EXTRATO ==========")
        if not self.extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(self.extrato)

        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print("=============================\n")

    def __repr__(self):
        return f"Agência {self.agencia} | Conta {self.numero} | Cliente: {self.cliente.nome}"


# ==========================================
#  GERENCIADOR PRINCIPAL DO BANCO
# ==========================================
class Banco:
    def __init__(self):
        self.clientes = []
        self.contas = []
        self.agencia = "0001"

    # -----------------------------------
    #        OPERAÇÕES DO BANCO
    # -----------------------------------
    def criar_cliente(self):
        print("\nCadastro de novo cliente")

        cpf = input("CPF: ")
        if self.buscar_cliente(cpf):
            print(f"{Cores.AMARELO}⚠️ Cliente já existe.{Cores.RESET}")
            return

        nome = input("Nome completo: ")
        nascimento = input("Data de nascimento: ")
        endereco = input("Endereço completo: ")

        novo = Cliente(nome, cpf, nascimento, endereco)
        self.clientes.append(novo)

        print(f"{Cores.VERDE}✅ Cliente criado com sucesso!{Cores.RESET}")

    def listar_clientes(self):
        if not self.clientes:
            print(f"{Cores.AMARELO}⚠️ Nenhum cliente cadastrado.{Cores.RESET}")
            return

        print("\n========== CLIENTES ==========")
        for cliente in self.clientes:
            print(f"Nome: {cliente.nome}")
            print(f"CPF: {cliente.cpf}")
            print(f"Data de Nascimento: {cliente.nascimento}")
            print(f"Endereço: {cliente.endereco}")
            print("-" * 30)

    def buscar_cliente(self, cpf):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente
        return None

    def criar_conta(self):
        cpf = input("\nCPF do cliente: ")
        cliente = self.buscar_cliente(cpf)

        if not cliente:
            print(f"{Cores.VERMELHO}❌ Cliente não encontrado.{Cores.RESET}")
            return

        numero_conta = len(self.contas) + 1
        conta = Conta(self.agencia, numero_conta, cliente)
        self.contas.append(conta)

        print(f"{Cores.VERDE}✅ Conta criada com sucesso!{Cores.RESET}")
        print(conta)

    def listar_contas(self):
        if not self.contas:
            print(f"{Cores.AMARELO}⚠️ Nenhuma conta cadastrada.{Cores.RESET}")
            return

        print("\n========== CONTAS ==========")
        for conta in self.contas:
            print(conta)

    def selecionar_conta(self):
        if not self.contas:
            print(f"{Cores.AMARELO}⚠️ Nenhuma conta para selecionar.{Cores.RESET}")
            return None

        self.listar_contas()

        try:
            numero = int(input("\nDigite o número da conta: "))
        except ValueError:
            print(f"{Cores.VERMELHO}❌ Entrada inválida.{Cores.RESET}")
            return None

        for conta in self.contas:
            if conta.numero == numero:
                return conta

        print(f"{Cores.VERMELHO}❌ Conta não encontrada.{Cores.RESET}")
        return None


# ==========================================
#  SISTEMA — MENU PRINCIPAL
# ==========================================
def limpar_console():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    banco = Banco()

    menu = f"""
{Cores.CIANO}{Cores.NEGRITO}========= MENU ========={Cores.RESET}
[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar cliente
[lu] Listar clientes
[c] Criar conta
[l] Listar contas
[q] Sair
=======================
"""

    while True:
        opcao = input(menu + "=> ").lower()

        if opcao == "u":
            banco.criar_cliente()

        elif opcao == "lu":
            banco.listar_clientes()

        elif opcao == "c":
            banco.criar_conta()

        elif opcao == "l":
            banco.listar_contas()

        elif opcao in ("d", "s", "e"):
            conta = banco.selecionar_conta()
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
            print(f"{Cores.VERDE}👋 Obrigado por usar o sistema bancário!{Cores.RESET}")
            break

        else:
            print(f"{Cores.VERMELHO}❌ Opção inválida!{Cores.RESET}")


if __name__ == "__main__":
    main()

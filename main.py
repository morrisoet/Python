from pessoa_fisica import PessoaFisica
from conta_corrente import ContaCorrente
from transacao import Deposito, Saque


def buscar_cliente(cpf, clientes):
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente
    return None


def criar_cliente(clientes):
    cpf = input("CPF: ")
    if buscar_cliente(cpf, clientes):
        print("⚠️ Cliente já existe.")
        return

    nome = input("Nome: ")
    data_nascimento = input("Data de nascimento: ")
    endereco = input("Endereço: ")

    cliente = PessoaFisica(nome, cpf, data_nascimento, endereco)
    clientes.append(cliente)

    print("✅ Cliente criado com sucesso!")


def criar_conta(clientes, contas):
    cpf = input("CPF do cliente: ")
    cliente = buscar_cliente(cpf, clientes)

    if not cliente:
        print("❌ Cliente não encontrado.")
        return

    numero = len(contas) + 1
    conta = ContaCorrente(cliente, numero)
    cliente.adicionar_conta(conta)
    contas.append(conta)

    print(f"✅ Conta {numero} criada com sucesso!")


def selecionar_conta(cliente):
    if not cliente.contas:
        print("⚠️ Cliente não possui contas.")
        return None

    for conta in cliente.contas:
        print(conta)

    numero = int(input("Número da conta: "))

    for conta in cliente.contas:
        if conta.numero == numero:
            return conta

    print("❌ Conta não encontrada.")
    return None


def main():
    clientes = []
    contas = []

    menu = """
========= MENU =========
[nu] Novo usuário
[nc] Nova conta
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
========================
=> """

    while True:
        opcao = input(menu).lower()

        if opcao == "nu":
            criar_cliente(clientes)

        elif opcao == "nc":
            criar_conta(clientes, contas)

        elif opcao in ("d", "s", "e"):
            cpf = input("CPF do cliente: ")
            cliente = buscar_cliente(cpf, clientes)

            if not cliente:
                print("❌ Cliente não encontrado.")
                continue

            conta = selecionar_conta(cliente)
            if not conta:
                continue

            if opcao == "d":
                valor = float(input("Valor do depósito: "))
                cliente.realizar_transacao(conta, Deposito(valor))

            elif opcao == "s":
                valor = float(input("Valor do saque: "))
                cliente.realizar_transacao(conta, Saque(valor))

            elif opcao == "e":
                conta.historico.mostrar()
                print(f"Saldo atual: R$ {conta.saldo:.2f}")

        elif opcao == "q":
            print("👋 Saindo...")
            break

        else:
            print("❌ Opção inválida.")


if __name__ == "__main__":
    main()

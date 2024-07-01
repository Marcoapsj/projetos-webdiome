import textwrap


class Cliente:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco


class Conta:
    LIMITE_SAQUES = 3

    def __init__(self, agencia, numero, cliente):
        self.agencia = agencia
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0
        self.limite = 500
        self.extrato = ""
        self.numero_saques = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito:\tR$ {valor:.2f}\n"
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    def sacar(self, valor):
        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > self.limite
        excedeu_saques = self.numero_saques >= Conta.LIMITE_SAQUES

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        elif excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque:\t\tR$ {valor:.2f}\n"
            self.numero_saques += 1
            print("\n=== Saque realizado com sucesso! ===")

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo:\t\tR$ {self.saldo:.2f}")
        print("=========================================")

    def solicitar_cartao(self):
        SALDO_ELEGIVEL = 1000

        if self.saldo < SALDO_ELEGIVEL:
            print(
                "Operação falhou! Para você verificar sua elegibilidade, seu saldo deve ser maior que 1000.")
        elif self.saldo <= 5000:
            print(
                "Você está elegível para solicitar apenas um cartão de crédito do tipo Platinum")
        else:
            print(
                "Você está elegível para solicitar apenas um cartão de crédito do tipo Black")


class Banco:
    AGENCIA = "0001"

    def __init__(self):
        self.usuarios = []
        self.contas = []

    def criar_usuario(self):
        cpf = input("Informe o CPF (somente número): ")
        usuario = self.filtrar_usuario(cpf)

        if usuario:
            print("\n@@@ Já existe usuário com esse CPF! @@@")
            return

        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input(
            "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        self.usuarios.append(Cliente(nome, data_nascimento, cpf, endereco))
        print("=== Usuário criado com sucesso! ===")

    def filtrar_usuario(self, cpf):
        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                return usuario
        return None

    def criar_conta(self):
        cpf = input("Informe o CPF do usuário: ")
        usuario = self.filtrar_usuario(cpf)

        if usuario:
            numero_conta = len(self.contas) + 1
            conta = Conta(Banco.AGENCIA, numero_conta, usuario)
            self.contas.append(conta)
            print("\n=== Conta criada com sucesso! ===")
        else:
            print(
                "\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

    def listar_contas(self):
        for conta in self.contas:
            linha = f"""\
                Agência:\t{conta.agencia}
                C/C:\t\t{conta.numero}
                Titular:\t{conta.cliente.nome}
            """
            print("=" * 100)
            print(textwrap.dedent(linha))


def menu():
    menu_texto = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [c]\tCartão de crédito
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu_texto))


def main():
    banco = Banco()

    while True:
        opcao = menu()

        if opcao == "d":
            numero_conta = int(input("Informe o número da conta: "))
            valor = float(input("Informe o valor do depósito: "))

            conta = banco.contas[numero_conta - 1]
            conta.depositar(valor)

        elif opcao == "s":
            numero_conta = int(input("Informe o número da conta: "))
            valor = float(input("Informe o valor do saque: "))

            conta = banco.contas[numero_conta - 1]
            conta.sacar(valor)

        elif opcao == "e":
            numero_conta = int(input("Informe o número da conta: "))
            conta = banco.contas[numero_conta - 1]
            conta.exibir_extrato()

        elif opcao == "nu":
            banco.criar_usuario()

        elif opcao == "nc":
            banco.criar_conta()

        elif opcao == "lc":
            banco.listar_contas()

        elif opcao == "c":
            numero_conta = int(input("Informe o número da conta: "))
            conta = banco.contas[numero_conta - 1]
            conta.solicitar_cartao()

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()

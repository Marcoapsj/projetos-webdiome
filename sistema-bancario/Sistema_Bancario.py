menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[c] Cartão de crédito
[q] Sair

=> """

saldo = 0
limite = 2000
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
SALDO_ELEGIVEL = 1000

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "c":

        if saldo < SALDO_ELEGIVEL:
            print(
                "Operação falhou! Para você verificar sua elegibilidade, seu saldo deve ser maior que 1000.")
        else:
            if saldo >= SALDO_ELEGIVEL and saldo <= 5000:
                print(
                    "Você está elegível para solicitar apenas um cartão de crédito do tipo platinum")
            else:
                print(
                    "Você está elegível para solicitar apenas um cartão de crédito do tipo Black")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

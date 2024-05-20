menu = ("""
============ MENU ===========
[1] - DEPOSITAR
[2] - SACAR
[3] - EXTRATO
[4] - SAIR
==============================
      """)

saldo = 0
limite = 500
saque = 3
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    if opcao == "1":
        valor = float(input("Informe o valor de depósito:"))
        print(f"Valor de R$ {valor:.2f} depositado em sua conta")
    
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor: .2f}\n"
        
        else:
            print("Operação falhou! O valor informado é invalido.")
    
    elif opcao == "2":
        valor = float(input("Qual valor do saque:"))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Você não possui saldo suficiente")

        elif excedeu_limite:
            print("Você ultrapassou seu limite de saque.")

        elif excedeu_saques:
            print("Número de saque execedido, volte amanhã")
    
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Valor de R$ {valor:.2f} sacado em sua conta")
        
        else:
            print("Valor informado é inválido!")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
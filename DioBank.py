print("[d] Depositar")
print("[s] Sacar")
print("[e] Extrato")
print("[q] Sair")


saldo = 0
limite = 500
numero_saques= 0
LIMITE_SAQUES = 3
extrato = ""

while True:
    opcao = str(input("Ensira o número do menu: "))
    if opcao == "d":
        print("Deposito")
        valor = float(input("Digite o valor do deposito: "))
        if(valor >0):
            saldo += valor
            print("Deposito realizado com sucesso!")
            extrato += f"Deposito: R$ {valor:.2f}\n"
        else:
            print("Valor invalido!")

    elif opcao == "s":
        print("Sacar")
        valor = float(input("Digite o valor do saque: "))
        if saldo >= valor and valor <= limite:
            if numero_saques <= LIMITE_SAQUES:
                numero_saques += 1
                saldo -= valor
                print("Saque realizado com sucesso!")
                extrato += f"Saque: R$ {valor:.2f}\n"

                
            else:
                print("Limite de saques atingido!")
                
        else:
            print("Saldo insuficiente!")
            
    elif opcao == "e":
        print(extrato)
        print(f"Saldo: R$ {saldo:.2f}")
    elif opcao == "q":
        print("Sair")
        break
    else:
        print("Opção Invalida")       
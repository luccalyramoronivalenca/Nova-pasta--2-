def sistema (saldo, modo):
    if modo == "saque":
        valor = float(input("Digite o valor do saque: "))
        if valor <= saldo:
            saldo -= valor
            print(f"Saque realizado com sucesso! Saldo atual: {saldo}")
        else:
            print("Saldo insuficiente para realizar o saque.")
    elif modo == "deposito":
        valor = float(input("Digite o valor do depósito: "))
        saldo += valor
        print(f"Depósito realizado com sucesso! Saldo atual: {saldo}")
    else:
        print("Modo inválido. Escolha 'saque' ou 'deposito'.")
    
    return saldo

print(sistema(1000, "saque"))
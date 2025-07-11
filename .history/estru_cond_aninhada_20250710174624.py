# Etapa 2: if aninhado

conta_normal = True
conta_universitaria = True
saldo = 500
saque = 200
cheque_especial = 100

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com cheque especial")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    else:
        print("Saldo insuficiente para saque")
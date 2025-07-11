""" 
Etapa 1: if, if-else, elif
Etapa 2: if aninhado
Etapa 3: if ternário
"""

# Etapa 1: if, if-else, elif

maior_idade = 18
idade_especial = 17
idade = int(input("Digite sua idade: ")) # treansforma a entrada em inteiro

if idade == idade_especial:
    print("Você ainda é menor de idade, mas pode assistir às aulas teóricas," 
        " contudo, ainda não pode dirigir")
elif idade < maior_idade:
    print("Você é menor de idade")
else:
    print("Você é maior de idade e pode dirigir")
    
print()

# Etapa 2: if aninhado
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
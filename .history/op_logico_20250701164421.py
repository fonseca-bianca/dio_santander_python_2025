saldo = 1000
saque = 250
limite = 200
conta_especial = True

(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
# output: True

# o ideal é quebrar a lógica em variáveis pra ficar mais legível
conta_comum_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

opcao_3 = (
            conta_comum_com_saldo_suficiente or
            conta_especial_com_saldo_suficiente
)   
# Em Python, a quebra de linha em atribuições de variáveis exige parênteses 
# quando a expressão continua na linha seguinte. Isso é uma regra sintática 
# da LP
print(opcao_3)
# Etapa 3: if ternário
# São 3 partes:
# 1. retorno:
#     caso a expressão retorne True
# 2. expressão lógica:
# 3. retorno:
#     caso a expressão retorne False

saldo = 500
saque = 200
status = "Sucesso" if saldo >= saque else "Saldo insuficiente"
print(f"{status} ao realizar o saque")
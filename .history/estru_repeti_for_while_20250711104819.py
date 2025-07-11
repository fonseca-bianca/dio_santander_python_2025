"""
Etapa 1. o que são estruturas de repetição?
Etapa 2. comando 'for' e a função 'built-in range()':
    for:
        quando sabemos quantas vezes o bloco de código vai ser executado
    range():
        início inclusivo e fim exclusivo, logo:
        0-10 (vai de 0-9)
        
        range(0, 15, 5) --> 0: start, 15: stop, 5: step
etapa 3. comando 'while':
    quando NÃO sabemos quantas vezes o bloco de código vai ser executado
"""

texto = input("Digite um texto: ")
vogais = "aeiou"
contador = 0

for letra in texto:
    if letra.lower() in vogais:
        contador +=1
        print(letra, end="") # não pular linha, continuar na mesma linha
print()

# OBS.:
#     quando é usado o 'input()' no 'for':
#         O Python não sabe antes quantas letras serão digitadas,
#         mas depois que o usuário digita, a string é formada.


print()

# while:
opcao = -1

while opcao != 0:
    opcao = int(input("[1] pra sacar \n[2] pra extrato \n[0] pra sair \n"))
    if opcao == 1:
        print("Saque efetuado")
    elif opcao == 2:
        print("Exibindo extrato...")
    else:
        print("Saindo do sistema")


# while com break:
while True:
    numero = int(input("Digite um número de 0 a 9: "))
    
    if numero == 10:
        break  # só sai do loop se usuário digitar 10
    
    print(numero)
    
# for com break:
for numero in range(100):
    if numero == 10:
        break
    
    print(numero, end=" ")  # imprime na mesma linha, separado por espaço
    
for numero in range(100):
    if numero == 12:
        continue # pula o número 12 e continua o loop
    
    print(numero, end=" ")
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

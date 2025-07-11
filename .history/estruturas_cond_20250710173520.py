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
    print("Você pode assistir às aulas teóricas, mas não poderá dirigir")
elif idade < maior_idade:
    print("Você é menor de idade")
else:
    print("Você é maior de idade e pode dirigir")
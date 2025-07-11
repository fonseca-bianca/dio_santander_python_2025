# Etapa 1: if, if-else, elif
        
maior_idade = 18
idade_especial = 17
idade = int(input("Digite sua idade: "))

if idade == idade_especial:
    print("Você é menor de idade, maspode assistir às aulas teóricas, "
          "contudo, não pode dirigir")

elif idade < maior_idade:
    print("Você é menor de idade")

else:
    print("Você é maior de idade e pode dirigir")
# Etapa 1: if, if-else, elif
        
maior_idade = 18
idade_especial = 17
idade = int(input("Digite sua idade: "))

if idade == idade_especial: # tem q vir antes pq se não entra no 'elif'
    print("Você é menor de idade, mas pode assistir às aulas teóricas, "
          "contudo, não pode dirigir")

elif idade < maior_idade:
    print("Você é menor de idade")

else:
    print("Você é maior de idade e pode dirigir")
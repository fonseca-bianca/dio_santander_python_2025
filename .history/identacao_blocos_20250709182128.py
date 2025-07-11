def sacar(valor):
    saldo = 500
    
    if saldo >= valor:
        print("O valor foi sacado")

    print("Obrigado por ser nosso cliente") 
# esse print está fora do bloco if, mas dentro da função 'sacar', portanto,
# vai ser lido após o print interno ser impresso
        
sacar(200) # 'valor' é o parâmetro da função 'sacar()' 
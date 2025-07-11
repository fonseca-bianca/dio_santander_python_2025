def sacar(valor):
    saldo = 500
    
    if saldo >= valor:
        print("O valor foi sacado")

    print("Obrigado por ser nosso cliente") 
# esse print está fora do bloco if, mas dentro da função 'sacar'
        
sacar(200) # 'valor' é o parâmetro da função 'sacar()' 
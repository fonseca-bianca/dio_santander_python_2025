def sacar(valor):
    saldo = 500
    
    if saldo >= valor:
        print("O valor foi sacado")

    print("Obrigado por ser nosso cliente") 
# esse print está fora do bloco if, mas dentro da função 'sacar', portanto,
# vai ser lido e tanto faz se o print dentro do 'if' é T ou F

def depositar(valor):
    saldo = 500
    saldo += valor
       
sacar(200) # 'valor' é o parâmetro da função 'sacar()' 
# sacar(1000) # NÃO vai ler, pq o valor sacado é maior do q o saldo
depositar()

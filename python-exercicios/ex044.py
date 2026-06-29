preco = float(input('Quanto custa o produto: R$'))  
pag = int(input('''1 - dinheiro
2 - cheque
3 - cartão
Qual o meio de pagamento: '''))

desconto = 0
juros = 0

if pag == 1 or pag == 2:
    desconto =  10
elif pag == 3:
    parc = int(input('Divide em quantas parcelas: '))
    if parc == 1:
        desconto = 5
    elif parc == 2:
        desconto = 0
    elif parc > 2:
        juros = 20
    else:
        print('Número de parcelas inválido')
else:
    print('Forma de pagamento não identificado')

def modificador():
    if desconto >= 0 and juros == 0:
        return f'Desconto: {desconto}%'
    elif juros > 0 and desconto == 0:
        return f'Juros: {juros}%'
    
if desconto >= 0 and juros == 0:
    preco_final = preco - (preco*(desconto/100))
elif juros > 0 and desconto == 0:
    preco_final = preco + (preco*(juros/100))

print()
print(f'Valor do produto: R${preco}')       #* valor original do produto
print(modificador())                        #* desconto ou juros 
print(f'Valor final: R${preco_final:.2f}')  #* valor final do produto
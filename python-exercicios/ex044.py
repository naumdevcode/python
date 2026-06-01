preco = float(input('Quanto custa o produto: R$'))
pag = int(input('''1 - dinheiro
2 - cheque
3 - cartão
Qual o meio de pagamento: '''))
def desconto():
    if pag == 1 or pag == 2:
        return 10
    elif pag == 3:
        parc = int(input('Divide em quantas parcelas: '))
        if parc == 1:
            return 5
        elif parc == 2:
            return 0
        elif parc > 2:
            return 0
        else:
            print('Número de parcelas inválido')
    else:
        print('Forma de pagamento não identificado')
print()
print(f'''Valor do produto: R${preco}
Desconto: {desconto()}%''')
preco_final = preco - (preco*(desconto()/100))
print(f'Valor final: R${preco_final:.2f}')
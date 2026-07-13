preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] - à vista dinheiro/cheque
[ 2 ] - à vista cartão
[ 3 ] - 2x no cartão
[ 4 ] - 3x ou mais no cartão''')
pag = int(input('Qual é a opção? '))
if pag == 1:
    total = preco - (preco * 0.1)
elif pag == 2:
    total = preco - (preco * 0.05)
elif pag == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de {parcela:.2f} SEM JUROS')
elif pag == 4:
    total = preco + (preco * 0.2)
    totparc = int(input('Quantas parcelas? '))
    parcela =  total / totparc
    print(f'Sua compra será parcelada em {totparc}x de R${parcela:.2f} COM JUROS')
else:
    total = preco
    print('OPÇÃO INVÁLIDA de pagamento. tente novamente!')
print(f'Sua compra de  R${preco:.2f} vai custar R${total:.2f} no final.')
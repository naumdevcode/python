dis = float(input('Quantos km é sua viagem: '))
if dis <= 200:
    pay = dis * 0.5
else:
    pay = dis * 0.45
print('O valor da sua passagem é R${:.2f}'.format(pay))
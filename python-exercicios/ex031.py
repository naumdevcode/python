dis = float(input('Quantos km é sua viagem: '))
pay = dis * 0.5 if dis <= 200 else dis * 0.45
print('O valor da sua passagem é R${:.2f}'.format(pay))
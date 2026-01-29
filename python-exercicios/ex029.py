vel = float(input('Digite a velocidade: '))
if vel > 80:
    multa = (vel - 80) * 7
    print('Você ultrapassou a velocidade permitida. \nVocê tomou uma multa de R${:.2f}'.format(multa))
print('Dirija sempre com cinto de segurança!')
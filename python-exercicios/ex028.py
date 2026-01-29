import random
ran = random.randint(0,5)
num = int(input('Adivinhe o meu número: '))
if num == ran: 
    print('Você acertou, PARABÉNS!')
else:
    print('Você errou! o número era {}'.format(ran))
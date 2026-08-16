from random import randint
from time import sleep
print('Sou seu computador...\nAcabei de pensar em um número entre 0 e 10.')
sleep(2)
print('Será que você consegue adivinhar qual foi?')
sleep(2)
bot = randint(0,10)
acertou = False
palpites = 0
while not acertou:
    player = int(input('Qual é seu palpite? '))
    palpites += 1
    if player < bot:
        print('Mais... Tente mais uma vez.')
    elif player > bot:
        print('Menos... Tente mais uma vez.')
    elif player == bot:
        acertou = True
print(f'Acertou com {palpites} tentativas. Parabéns!')
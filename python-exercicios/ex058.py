from random import randint
from time import sleep
print('-=-' * 20)
print('Vou pensar em um número entre 1 e 10. Tente adivinhar...')
print('-=-' * 20)
bot = randint(1,10)
player = int(input('Em que número eu pensei? '))
tentativas = 1
print('Procesando...')
sleep(3)
while player != bot:
    player = int(input('Errou. Tente novamente: '))
    tentativas += 1
    print('Processando...')
    sleep(1)
print(f'PARABÉNS! Você conseguiu na {tentativas}ª tentativa')
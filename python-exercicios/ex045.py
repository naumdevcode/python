from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções:
[ 0 ] - PEDRA
[ 1 ] - PAPEL
[ 2 ] - TESOURA''')
jogador = int(input('Qual sua jogada? '))
if jogador > 2:
    print('JOGADA INVÁLIDA. tente novamente')
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    print('-=' * 12)
    print(f'Computador jogou {itens[computador]}')
    print(f'Jogador jogou {itens[jogador]}')
    print('-=' * 12)
    if computador == jogador:
        print('EMPATE')
    elif (computador == 0 and jogador == 2) or (computador == 1 and jogador == 0) or (computador == 2 and jogador == 1):
        print('COMPUTADOR VENCE')
    else:
        print('JOGADOR VENCE')
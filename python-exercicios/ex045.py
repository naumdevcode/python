from random import randint
print('------VAMOS JOGAR------')
bot = randint(1,3)
player = int(input('''1 - PEDRA
2 - PAPEL
3 - TESOURA
Qual você escolhe: '''))
    
if bot == 1:
    gbot = 'PEDRA'
elif bot == 2:
    gbot = 'PAPEL'
elif bot == 3:
    gbot = 'TESOURA'

if player == 1:
    gplayer = 'PEDRA'
elif   player == 2:
    gplayer = 'PAPEL'
elif   player == 3:
    gplayer = 'TESOURA'

print(f'Eu escolho: {gbot}')
print(f'Você escolheu: {gplayer}')

if bot == player:
    print('EMPATAMOS!')
elif (bot == 1 and player == 3) or (bot == 2 and player == 1) or (bot == 3 and player == 2):
    print('VOCÊ PERDEU!')
else:
    print('VOCÊ GANHOU!')
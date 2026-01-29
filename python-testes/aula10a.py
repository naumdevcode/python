nome = str(input('Como você se chama? ')).upper().strip()
if nome == 'NAUM':
    print('Que nome lindo!')
else:
    print('Seu nome é normal')
print('Prazer em conhecer, {}!'.format(nome))
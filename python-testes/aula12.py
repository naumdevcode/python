Negrito = '\033[1m'
sublinhado = '\033[4m'
Fbranco = '\033[7m'
limpa = '\033[m'
nome = str(input('{}Qual é o seu nome? {}'.format(Negrito,Fbranco)))
print(limpa,end='')
if nome.lower() == 'naum':
    print('Que nome bonito')
else:
    print('Que nome normal')
print('Tenha um bom dia, {}{}{}!'.format(sublinhado,nome,limpa))
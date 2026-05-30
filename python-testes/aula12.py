Negrito = '\033[1m'
sublinhado = '\033[4m'
Fbranco = '\033[7m'
limpa = '\033[m'
nome = str(input('{}Qual é o seu nome? {}'.format(Negrito,Fbranco)).strip().lower())
print(limpa,end='')
if nome == 'naum':
    print('Que nome bonito')
elif nome == 'joao' or nome == 'maria' or nome == 'pedro':
    print('Seu nome é bem popular no Brasil')
elif nome in 'ana leticia duda magnolia ariele':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia, {}{}{}!'.format(sublinhado,nome,limpa))
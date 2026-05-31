num = int(input('Digite um número: '))
conv = int(input('1 - Binário \n2 - Octal \n3 - Hexadecimal \nEscolha qual será a base de conversão: '))

if conv >= 1 and conv <=3:
    print(f'{num}')
    print(f'{conv}')
else:
    print('[ERRO]')
